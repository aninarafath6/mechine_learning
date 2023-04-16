def get_details(arr ,callback = None):
    print("array:\n",arr)
    print("size: ",arr.size)
    print("Dimension: ",arr.ndim)
    print("Shape: ",arr.shape)
    print("Type: ",arr.dtype)
    print("Item Size: ",arr.itemsize)
    if callback is not None:
            callback(arr)


# properties of complex data
def cdts(arr): 
    print("Imaginary: "+str(arr.imag))
    print("Real: "+str(arr.real))