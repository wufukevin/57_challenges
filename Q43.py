import RegulationFunction as rf
import os


class WebsiteGenerator:
    def __init__(self, siteName, author, wantJsFolder, wantCssFolder):
        self.siteName = siteName
        self.author = author
        self.wantJsFolder = wantJsFolder == 'y'
        self.wantCssFolder = wantCssFolder == 'y'

        self.cur_path = os.path.abspath(os.path.dirname(__file__))


    @classmethod
    def fromInput(cls):
        return cls(
            rf.InputFunction('Site name: '),
            rf.InputFunction('Author: '),
            rf.InputFunction('Do you want a folder for JavaScript? ', 1, rf.isYesOrNo),
            rf.InputFunction('Do you want a folder for CSS? ', 1, rf.isYesOrNo)
        )

    def generateWeb(self):
        sitePath = os.path.abspath(self.cur_path + f'/{self.siteName}')
        self.createFolder(sitePath)
        # if not os.path.exists(sitePath): os.mkdir(sitePath)
        # print(f'Created ./{self.siteName}')

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
        file = open(f"{sitePath}/index.html", "w")
        file.write(text)
        file.close()
        print(f'Created {sitePath}/index.html')


        if self.wantJsFolder:
            jsPath = os.path.abspath(f'{sitePath}/js')
            self.createFolder(jsPath)
        if self.wantCssFolder:
            cssPath = os.path.abspath(f'{sitePath}/css')
            self.createFolder(cssPath)

    def createFolder(self, folderPath):
        if not os.path.exists(folderPath): os.mkdir(folderPath)
        print(f'Created {folderPath}')


mainFunction = WebsiteGenerator.fromInput()
mainFunction.generateWeb()
