class Movie:
    
    def __init__(self,name,released_date,collection = None):
        
        self.__name = name #private data
        self.__released_date = released_date #private data
        self.collection = collection
        
    def set_new_collection(self,new_collection):
        self.collection = new_collection
        
    def get_year(self,year):
        return self.__released_date >= year
        
    def getDetails(self):
        return f"Movie name : {self.__name}, Released Date : {self.__released_date}, Box office Collection : {self.collection if self.collection is not None else 'not available'}\n"
        

movie_list = [Movie("Spider Man",2010,"100M $"),
              Movie("Avatar2", 2023, "1B $"),
              Movie("Dune",2022, "100M $"),
              Movie("openhimer",2023)]   
    
for movie in movie_list:
    if(movie.get_year(2020)):
        # print(movie.__name) name is not accessible directly because it is declared as private
        print(movie.getDetails())

        
    
    