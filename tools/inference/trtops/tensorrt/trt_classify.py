import time
import numpy as np
import tensorrt as trt

import pycuda.autoinit
import pycuda.driver as cuda
    

def classify(pipe, *, engine, batch_size=1):

    # prepare the bindings
    # h_input, h_output - host input and output
    # d_input, d_output - device input and output
    ishape = engine.get_binding_shape("image")
    itype = trt.nptype(engine.get_binding_dtype("image"))
    h_input = np.empty(shape=ishape, dtype=itype)
    d_input = cuda.mem_alloc(h_input.nbytes)
    
    oshape = engine.get_binding_shape("preds")
    otype = trt.nptype(engine.get_binding_dtype("preds"))
    h_output = np.empty(shape=oshape, dtype=otype)
    d_output = cuda.mem_alloc(h_output.nbytes)
    
    bindings = [int(d_input), int(d_output)]
    
    # create the execution context for the engine
    context = engine.create_execution_context()
    stream = cuda.Stream()
    
    # run the loop
    total_time = 0
    
    for item in pipe:
        start = time.time()
        
        image = item['image']
        
        cuda.memcpy_htod_async(d_input, image, stream)
        context.execute_async_v2(bindings, stream.handle, None)
        cuda.memcpy_dtoh_async(h_output, d_output, stream)
        stream.synchronize()
        
        item['preds'] = np.copy(h_output)

        total_time += (time.time() - start)
        item['inference_time'] = total_time
        
        yield item

