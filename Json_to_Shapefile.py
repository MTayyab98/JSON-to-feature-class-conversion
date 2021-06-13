import arcpy
import os
os.chdir("D:\\tayyab\\New folder\\Canal\\data\\data")
arcpy.env.workspace = "D:\\tayyab\\New folder\\Canal\\data\\data"
arcpy.env.overwriteOutput = True
arr = os.listdir('.')   #returns a list containing the names of the entries in the directory

for i in arr:   
    arcpy.JSONToFeatures_conversion(i, ("output3{}.shp").format(i)) #converts JSON to Feature class
    
