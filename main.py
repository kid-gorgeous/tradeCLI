# Thank you for previewing this snippet of my project. It is the main file, and requires the other files to run.
# It provides a primitive user interface, and a primitive command line interface for the user to interact with.
# It also provides a dataset class, and an exchange class. The exchange class is the most important, as it will 
#    interact with the coinbase API and CLI to commit user interactions.


# Helper function to install requirements from requirements.txt file
import subprocess
def install_requirements(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    stdout = process.communicate()


if __name__ == "__main__":

    # make preparations for compilation
    install_requirements('pip3 install -r requirements.txt')
    from dataset import dataset
    import keys as k


    # Get the symbols, and create the dataset from user provided information (primitive user functionality)
    # symbols = input("Enter symbols: ").split()
    symbols = ['BTC-USD', 'ETH-USD', 'DOGE-USD']    # A list of popular symbols on coinbase
    data = dataset(symbols)


    # Connect to the exchange, and point to api keys. Sets the client for the exchange. 
    from exchange import Order as ex
    api, secret = k.getKeys()
    ex = ex(symbols[0], 1, data.gbp(), 'buy')
    ex.setClient(api, secret)


    # Import some User Information to initialize the CLI. (primitive user functionality)
    #  This will require an input, and an API key and secret key. For now, you must
    #  manually enter the API key and secret key in a keys.py file. 
    from cmd import Cli
    cmd = Cli()                                     # Create a new instance of the CLI
    cmd.user_info()                                 # returns a tuple
    cmd.accounts()                                  # returns a list of tuples


    
