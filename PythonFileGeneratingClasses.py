"""
Created on Nov 2, 2022

    PythonFileGeneratingClasses.py contains the PythonFileWriter Class, which contains the read, write, and combine
functions for PythonFileWriter.

@author: lborcherding
"""

import random

# *IMPORTANT NOTICE* PythonFileWriter Module, AKA Class Can be Imported as Class to other scripts, or run directly through main.
# -------------------------------------------------------------------------------------------------
class PythonFileWriter:

    def __init__(self):
        """
        Default Constructor
        """
        return None

    # -------------------------------------------------------------------------------------------------
    def WriteStorageDictJson( self, writeJsonPath, portionOneDict, portionTwoDict, fileName):
        """ A Function which takes the self.__storageDict from the Perform function, and writes
        the file data to the file named StorageDict.json
        Args:
            mapFile, wizDict
        Returns:
            fileLengthDict
        """

        # Check for empty dict
        if portionOneDict == {}:
            pass
        else:
            # if not empty get last key
            lastKeyONE = list(portionOneDict.keys())[-1]

        # Check for empty dict
        if portionTwoDict == {}:
            pass
        else:
            # if not empty get last key
            lastKeyTWO = list(portionTwoDict.keys())[-1]

        # remove file type from name string
        fileName = fileName.split('.')[0]

        # Set Values
        keyIndexNum = -1
        columns = 1

        # Open the Json file, and write with the storageDict data
        with open( f"{writeJsonPath}", "w" ) as writeJsonObject:

            # Open Dictionary
            writeJsonObject.truncate(0)
            writeJsonObject.write("{\n")

            # for keys
            for key in portionOneDict:
                keyIndexNum += 1
                #write data in string format
                writeJsonObject.write("    ")
                writeJsonObject.write('"')
                writeJsonObject.write(f'$({key}.{fileName})')
                writeJsonObject.write('"')
                writeJsonObject.write(' : ')
                writeJsonObject.write('"')
                writeJsonObject.write(f'{portionOneDict[key]}')
                writeJsonObject.write('"')
                # skip comma for last key
                if key == lastKeyONE:
                    writeJsonObject.write(',')
                    pass
                else:
                    writeJsonObject.write(',')

                if (keyIndexNum+1) % columns == 0 :
                    writeJsonObject.write("\n")

            for key in portionTwoDict:
                keyIndexNum += 1
                #write data in string format
                writeJsonObject.write("    ")
                writeJsonObject.write('"')
                writeJsonObject.write(f'$({key}.{fileName})')
                writeJsonObject.write('"')
                writeJsonObject.write(' : ')
                writeJsonObject.write('"')
                writeJsonObject.write(f'{portionTwoDict[key]}')
                writeJsonObject.write('"')
                # skip comma for last key
                if key == lastKeyTWO:
                    pass
                else:
                    writeJsonObject.write(',')

                if (keyIndexNum+1) % columns == 0:
                    writeJsonObject.write("\n")

            # Close Dictionary
            writeJsonObject.write("\n}")

        return None

    # -------------------------------------------------------------------------------------------------
    def ReadJsonDict( self, readJsonPath):
        """ A function for reading the data from the template json file which contains the default hex header data,
        variable data values are replaced later.

        #TODO Create modular regular expression based on the character occurence rate, ex:
            def readRandomFile (randomFilePath):
                with open randomFilePath :
                    for line in randomFilePath count all ascii characters, for highest occuring, or most

        Args:
            writeJsonPath
        Returns:
            readFileDict
        """
        # initialize dictionary
        readFileDict = {}

        # read json file key value pairs & store in dictionary
        with open(f"{readJsonPath}", "r") as readJsonObject:

            # for each line in the json file search for 4 match groups
            for (count, line) in enumerate(readJsonObject):

                # search line in imageHeaderDict.json for 4 match groups, groups 1 & 3 are the dict keys, where as groups 2 & 4 are the dict values
                match = re.search(r'"(\$\([A-Za-z0-9\S]+\))" : "([A-Za-z0-9\S]+)"', line)
                # match = re.search(r'"(\$\([A-Za-z0-9_]+))" : "([A-Za-z0-9_]+)"', line)
                # if match is found store groups in readFileDict
                if match:
                    # set key value pairs in readFileDict
                    readFileDict[match.group(1)] = match.group(2)

            # close file
            readJsonObject.close()
        return readFileDict

    # -------------------------------------------------------------------------------------------------
    def CombineJsonDictFiles(self, frontJsonData, backJsonData, writeJsonPath, fileName):
        """ A Function which takes the self.__storageDict from the Perform function, and writes
        the file data to the file named StorageDict.json
        Args:
            mapFile, wizDict
        Returns:
            fileLengthDict
        """
        # read json files and store data in dictionary
        frontJsonDataDict = self.ReadJsonDict(frontJsonData)
        backJsonDataDict = self.ReadJsonDict(backJsonData)

        # write front and back dict data to the given file path
        self.WriteStorageDictJson(writeJsonPath, frontJsonDataDict, backJsonDataDict, fileName)

        return None

# -------------------------------------------------------------------------------------------------
def main():
    # code that should only be executed when this module is run directly
    print("This is the main function")

    #TODO SETUP FILE PATH DICTIONARY ========================

    # Store the Following File paths in a json file
    Path_Config_String = 'D:\\CodingGit_StorageHDD\\PythonGit\\PythonFileWriter\\Config_file_storage\\filePaths.json'
    read_write_python_file_OUTPUT_Arg = 'D:\\CodingGit_StorageHDD\\PythonGit\\PythonFileWriter\\CustomFileFactory\\Output_Script.py'

    # Files paths
    filePathDict = {
        '1': '2',
        '2': '3',
        '3': '5',
        '4': '7',
        '5': '11',
        '6': '13',
        '7': '17',
        '8': '19'
    }

    # Second Dict #TODO last value has comma when dict is empty
    emptyDict = {
        'pathConfigString': f'{Path_Config_String}',
        'readWritePythonFileOutputArg': f'{read_write_python_file_OUTPUT_Arg}'
    }

    # filename string
    fileNameString = 'filePaths.json'

    # Write the above dictionary to a json file
    pythonWriter = PythonFileWriter()
    pythonWriter.WriteStorageDictJson(
        writeJsonPath=Path_Config_String,
        portionOneDict=filePathDict,
        portionTwoDict=emptyDict,
        fileName=fileNameString
    )

    #TODO Add readDict function call in main to print filePaths.json content.

    #Now you attach the PythonFileWriter Class to your existing program and call write, read, or combine to get
    #information from the various symbols in filepath.json. or insantiate a new instance of the write method with
    #a new file path to generate more custom .json files in the Config_file_storage

# ==================================================================================================================
if __name__ == "__main__":
    #Call main() function
    main()

# ==================================================================================================================