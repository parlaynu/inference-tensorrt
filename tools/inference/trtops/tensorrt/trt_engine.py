import tensorrt as trt


def load_engine(engine_path):
    print("loading engine...", flush=True)
    
    # load the engine archive
    with open(engine_path, "rb") as f:
        runtime = trt.Runtime(trt.Logger(trt.Logger.WARNING)) 
        engine = runtime.deserialize_cuda_engine(f.read())

    return engine


def get_binding_shape(engine, name):
    return list(engine.get_binding_shape(name))

def get_binding_dtype(engine, name):
    return trt.nptype(engine.get_binding_dtype("image"))

