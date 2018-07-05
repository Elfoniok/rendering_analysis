




## ======================= ##
##
class RenderParams:
    
    ## ======================= ##
    ##
    def __init__( self ):
    
        # Set default params.
        self.seed = 100
        self.inc_seed = 0
        self.start = 4225
        self.end = 6725
        self.step = 100
        self.width = 800
        self.height = 600
        

params_map = dict()

# barcelona
params_map[ "barcelona" ] = RenderParams()
params_map[ "barcelona" ].width = 800
params_map[ "barcelona" ].height = 600
params_map[ "barcelona" ].start = 5125
params_map[ "barcelona" ].end = 8725

# bunkbed
params_map[ "bunkbed" ] = RenderParams()
params_map[ "bunkbed" ].width = 800
params_map[ "bunkbed" ].height = 600
params_map[ "bunkbed" ].start = 6025
params_map[ "bunkbed" ].end = 8225

# cat
params_map[ "cat" ] = RenderParams()
params_map[ "cat" ].width = 1600
params_map[ "cat" ].height = 1200
params_map[ "cat" ].start = 3825
params_map[ "cat" ].end = 5825

# habitacion
params_map[ "habitacion" ] = RenderParams()
params_map[ "habitacion" ].width = 800
params_map[ "habitacion" ].height = 600
params_map[ "habitacion" ].start = 2825
params_map[ "habitacion" ].end = 3325

# mug
params_map[ "mug" ] = RenderParams()
params_map[ "mug" ].width = 800
params_map[ "mug" ].height = 600
params_map[ "mug" ].start = 3825
params_map[ "mug" ].end = 6325

# plushy
params_map[ "plushy" ] = RenderParams()
params_map[ "plushy" ].width = 400
params_map[ "plushy" ].height = 300
params_map[ "plushy" ].start = 4225
params_map[ "plushy" ].end = 6725

# sea
params_map[ "sea" ] = RenderParams()
params_map[ "sea" ].width = 800
params_map[ "sea" ].height = 600
params_map[ "sea" ].start = 825
params_map[ "sea" ].end = 4025

# tree
params_map[ "tree" ] = RenderParams()
params_map[ "tree" ].width = 800
params_map[ "tree" ].height = 600
params_map[ "tree" ].start = 425
params_map[ "tree" ].end = 2225


## ======================= ##
##
def get_scene_parameters( scene ):

    try:
        return params_map[ scene ]
    except:
    
        print( "Parameters for scene: [" + scene + "] aren't defined. Using default values. " )
        return RenderParams()


## ======================= ##
##
def print_scene_parameters( params ):

    print( "Width:          " + str( params.width ) )
    print( "Height          " + str( params.height ) )
    print( "Samples start:  " + str( params.start ) )
    print( "Samples end:    " + str( params.end ) )
    print( "Samples step:   " + str( params.step ) )
    print( "Seed:           " + str( params.seed ) )
    print( "Seed increment: " + str( params.inc_seed ) )


