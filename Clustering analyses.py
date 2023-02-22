import numpy as np

class matrix(object):

    def __init__(self,file):   # init function which will be called automatucally while creating object of the class
        self.array_2d = np.empty((0,0))
        self.load_from_csv(file)
        self.standardise()
    

    def load_from_csv(self,file_name):  # Read CSV file and load data into numpy two dimentional array
        with open(Users/daisysekar/Documents/Personal Document/FASER Export/CE705-7-AU/file_name , 'r') as file:
            self.array_2d = np.loadtxt(file, delimiter = ',')
            #print(self.array_2d)
            

    def standardise(self):  # Standardising the 2 dimentional array into -1 to 1
        average_column = np.mean(self.array_2d, axis =0) 
        column_max = np.max(self.array_2d, axis = 0)
        column_min = np.min(self.array_2d, axis = 0)

        for row in range(len(self.array_2d)):
            for column in range(len(self.array_2d[row])):
                self.array_2d[row][column] = (self.array_2d[row][column] - average_column[column])/(column_max[column] -column_min[column])
        #print(self.array_2d

    def get_distance(self,other_matrix,weights,beta): # This method will calculate the Euclidean distance between centroids and data matrix
        d = np.ones((self.centroids.shape[0],1))
        for i in range(self.centroids.shape[0]):
            d[i] = np.sum((weights**beta) * (self.centroids[i] - other_matrix)**2)
        min = np.min(d)
        
        for i in range(len(d)):
            if d[i] == min:
                return i    # Returning the index of centroid which has minimum distance 
        

    def get_count_frequency(self):  # counting the output of clusters in the form of dictionary
        unique, counting_num = np.unique(self.S, return_counts= True)
        return dict(zip(unique,counting_num))



# ****************************************** Function starts here ***************************




def get_initial_weights(m): # This function will retuen the random numbers inbetween 0 to 1 and sum of random numbers will be 1
    m = np.random.dirichlet(np.ones(m),size=1)
    #print(np.sum(m))
    return m




def get_centroids(m,S,K): # Calculating the centroids
    
    result = []
    for k in range(K):
        new_centroid_cluster = []
        for j in range((S.shape[0])):
            if S[j,0] == k:
                new_centroid_cluster.append(m.array_2d[j])
        result.append(np.mean(np.array(new_centroid_cluster),axis = 0))        
    return  np.array(result)
        
        
            


def get_groups(m,K,Beta): # This function will calculate and return the value of each row which belongs to which clusters

    
    row_count = m.array_2d.shape[0]  # number of rows in data matrix

    column_count = m.array_2d.shape[1]  # number of columns in data matrix
    
    weights = get_initial_weights(column_count) # initializing weights 

    m.centroids = np.empty((0,0)) # creates Centroids as empty matrix

    m.S = np.zeros((row_count,1)) # creates nd initialize zeros to S matrix 

    m.centroids = np.random.permutation(m.array_2d)[:K] # getting random row from data matrix with respect to K value

    
    while(True):
        S1 = m.S.copy()
        for i in range(len(m.array_2d)):
                m.S[i] = m.get_distance(m.array_2d[i],weights,Beta)
        if (m.S != S1).all(): 
            m.centroids = get_centroids(m,m.S,K)
            weights = get_initial_weights(column_count)
            
        else:
            return m

def run_test():
   m = matrix('Data.csv')
   for k in range(2,5):
       for beta in range(11,25):
           S = get_groups(m, k, beta/10)
           
           print(str(k)+'-'+str(beta)+'='+str(S.get_count_frequency()))


if __name__ == "__main__": # starting of main function

    run_test()

    
        
    
        
        

    
    








    
        
                
                
                
                
        
            
            
        
