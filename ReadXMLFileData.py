from bs4 import BeautifulSoup

class DataRead:
    
    def findTag(self, file, tagname):
        # Reading the data inside the xml
        # file to a variable under the name
        # data
        with open(file, 'r') as f:
            data = f.read()

        # Passing the stored data inside
        # the beautifulsoup parser, storing
        # the returned object
        Bs_data = BeautifulSoup(data, "xml")

        # Finding all instances of tag
        # `unique`
        tagdata = Bs_data.find_all(tagname)
        return tagdata

    def findvalue(file, Tagname, AttributeName, AttributeValue, AttributeReturnName):
        # Reading the data inside the xml
        # file to a variable under the name
        # data
        with open(file, 'r') as f:
            data = f.read()

        # Passing the stored data inside
        # the beautifulsoup parser, storing
        # the returned object
        Bs_data = BeautifulSoup(data, "xml")


        # Using find() to extract attributes
        # of the first instance of the tag
        b_name = Bs_data.find(Tagname, {AttributeName:AttributeValue})

        #print(b_name)

        # Extracting the data stored in a
        # specific attribute of the
        # `child` tag
        value = b_name.get(AttributeReturnName)
        return value
        print(value)
