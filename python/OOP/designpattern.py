# Template Method Pattern
class FileFormat(ABC):
    	@abstractmethod
	def datasetprocessor(self):
		pass
	def fileUpdate(self):
		pass
	def logic(self):
		self.datasetprocessor()
		self.fileUpdate()

class SaveXLSX(FileFormat):
	def __init__(self, file):
		self.file = file # Get Excel File name 
	def datasetprocessor(self):
		print("===========================================")
		# print("file",self.file)
		print("saving XLSX")
		# Read and store content of an excel file 
		read_file = pd.read_excel(self.file)

		filename = secure_filename(self.file.filename)
		filename = filename.split(".")[0]+".csv"

		# Write the dataframe object into csv file
		read_file.to_csv (os.path.join(app.config['UPLOAD_FOLDER'], filename), 
						index = None,
						header=True)
		print("===========================================")
		print("XLSX File saved successfully")
	def fileUpdate(self):
		pass

context = SaveCSV(file)
context.logic()

# Strategy Pattern
class Strategy(ABC):
    @abstractmethod
    def trainml(self):
        pass
    
    @abstractmethod
    def anomalydetection(self):
        pass
    
class Context():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def logic(self) -> None:
        self._strategy.trainml()
        self._strategy.anomalydetection()
        
class randomforest(Strategy):
    def __init__(self) -> None:
        pass 
    def anomalydetection(self):
        pass
    def trainML(self):
        try:
            pass
        except:
            pass