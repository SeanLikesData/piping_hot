# a module for restructuring nested function calls as easier-to-read pipelines
class Pipeline:
    """
    A class for creating and executing data processing pipelines.

    This class allows for the creation of pipelines that can process any object type
    (e.g., float, Pandas DataFrame, list) through a series of functions.

    Attributes:
        package: The package (object) being moved through the pipeline and iterated on by each function.
        Think of the package as a toy getting moved through an assembly line by conveyor belts.

    Methods:
        __init__(pipeline_target): Initializes the Pipeline with a target object.
        
        pipe(func, *args, **kwargs): Applies a function to the current value.
        
        result(): Returns the final result of the pipeline.
    
    Why use this?
    Nested functions are hard to read. In this format, you read from top to bottom, each pipe is a process getting applied to the package and it's output is what goes to the next pipe.
    
    Useage Example:
        def add(package, var):
            return package + var
        def subtract(package, var):
            return package - var
        def multiply(package, var):
            return package * var
        
        result = (
                Pipeline(5) 
                .pipe(multiply, 2) 
                .pipe(subtract, 3) 
                .result()
                )
        print(result)
    """

    def __init__(self, package_initial_value):
        self.package = package_initial_value

    def pipe(self, func, *args, **kwargs):
        self.package = func(self.package, *args, **kwargs)
        return self

    def result(self):
        return self.package

