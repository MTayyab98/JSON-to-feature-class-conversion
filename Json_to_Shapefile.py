import arcpy
import os
#os.chdir("D:\\tayyab\\New folder\\Canal\\data\\data")
#arcpy.env.workspace = "D:\\tayyab\\New folder\\Canal\\data\\data"    #Initialising workspace
arcpy.env.overwriteOutput = True     #For overwriting output if running code multiple times
arr = os.listdir('.')   #returns a list containing the names of the entries in the directory

for i in arr:          #Gives the output in the same directory
    arcpy.JSONToFeatures_conversion(i, ("output3{}.shp").format(i)) #converts JSON to Feature class
    
