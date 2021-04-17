import RegulationFunction as rf
import os


class WebsiteGenerator:
    def __init__(self, siteName, author, wantJavaFolder, wantCssFolder):
        self.siteName = siteName
        self.author = author
        self.wantJavaFolder = True if wantJavaFolder == 'y' else False
        self.wantCssFolder = True if wantCssFolder == 'y' else False

        self.cur_path = os.path.abspath(os.path.dirname(__file__))


    @classmethod
    def fromInput(cls):
        return cls(
            rf.InputFunction('Site name: '),
            rf.InputFunction('Author: '),
            rf.InputFunction('Do you want a folder for JavaScript? ',1,rf.isYesOrNO),
            rf.InputFunction('Do you want a folder for CSS? ',1,rf.isYesOrNO)
        )

    def generateWeb(self):
        data_path = os.path.abspath(self.cur_path + '/awesomeco')
        if not os.path.exists(data_path): os.mkdir(data_path)
        print('Created ./awesomeco')

        text = f'''
        <html>
            <head>
            <title>{self.siteName}</title>
            <meta name="author" content="{self.author}">
            </head>
            <body>
                <h1>Hello</h1>
            </body>
        </html>
        '''
        file = open("index.html", "w")
        file.write(text)
        file.close()
        print('Created ./awesomeco/index.html')

        if self.wantJavaFolder:
            data_path = os.path.abspath(self.cur_path + '/js')
            if not os.path.exists(data_path): os.mkdir(data_path)
            print('Created ./awesomeco/js/')
        if self.wantCssFolder:
            data_path = os.path.abspath(self.cur_path + '/css')
            if not os.path.exists(data_path): os.mkdir(data_path)
            print('Created ./awesomeco/css/')




mainFunction = WebsiteGenerator.fromInput()
mainFunction.generateWeb()
