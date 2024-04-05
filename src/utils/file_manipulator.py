
# python class to manipulate files
class FileManipulator:
    def __init__(self, filename):
        self.filename = filename

    def open_file(self):
        try:
            self.file = open(self.filename, 'w+')
            print(f"File '{self.filename}' opened successfully.")
        except Exception as e:
            print(f"Error opening file '{self.filename}': {e}")

    def write_to_file(self, data):
        if hasattr(self, 'file'):
            try:
                self.file.write(data)
                # print("Data written to the file.")                
            except Exception as e:
                print(f"Error writing to file '{self.filename}': {e}")
        else:
            print("File not opened. Call 'open_file()' before writing.")

    def close_file(self):
        if hasattr(self, 'file'):
            try:
                self.file.close()
                print(f"File '{self.filename}' closed.")
            except Exception as e:
                print(f"Error closing file '{self.filename}': {e}")
        else:
            print("No file to close.")
    
    def get_file(self):
        if hasattr(self, 'file'):
            print(f"File '{self.filename}' returned.")
            return self.file
        else:
            print("No file to return.")


    def read_file(self, line_number):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()

            if 1 <= line_number <= len(lines):
                line_content = lines[line_number - 1]

                # Check if the line is a comment
                if line_content.startswith("#") or line_content.startswith(" "):
                    print("Line is a comment")
                    return None

                return line_content

            print(f"Invalid line number: {line_number}")
            return None

        except FileNotFoundError:
            print(f"File '{self.filename}' not found")
            return None

        except Exception as e:
            print(f"Error reading file '{self.filename}': {e}")
            return None

    def read_file_content(self, line_number):
        with open(self.filename, 'r') as file:
            lines = file.readlines()

        matrix = []
        for line in lines[line_number - 1:]:
            matrix.extend(map(int, line.split()))
        
        return matrix
        
