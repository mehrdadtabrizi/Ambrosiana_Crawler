#Paramaters for the Ambrosiana Web Crawler
KEYWORD = "Adoration"
Iconography = "Adoration"

Header   = ['Branch',
            'File Name',
            'Image ID',
            'Artist',
            'Title',
            'Iconography',
            'Part',
            'Earliest Date',
            'Latest Date',
            'Margin Years',
            'Genre',
            'Material',
            'Medium',
            'Height of Image Field',
            'Width of Image Field',
            'Type of Object',
            'Height of Object',
            'Width of Object',
            'Diameter of Object',
            'Position of Depiction on Object',
            'Current Location',
            'Repository Number',
            'Original Location',
            'Original Place',
            'Original Position',
            'Context',
            'Place of Discovery',
            'Place of Manufacture',
            'Associated Scenes',
            'Related Works of Art',
            'Type of Similarity',
            'Inscription',
            'Text Source',
            'Bibliography',
            'Photo Archive',
            'Image Credits',
            'Details URL',
            'Additional Information']


Firefox_Driver_PATH = "C:\geckodriver.exe"
CSV_File_PATH       = 'Ambrosiana_Metadaten (' + KEYWORD + ').csv'
LINKS_File_PATH     = 'Ambrosiana_Links_' + KEYWORD + '.txt'
Images_PATH         = 'D:\_DATA\HiWiDateien\Crawler\Downloaded Images\_Anbetung, Adoration\Ambrosiana\ '

base_url    = 'https://collections.library.nd.edu'
search_URL  = 'https://collections.library.nd.edu/2d498adc70/' \
              'inventory-catalog-of-the-drawings-in-the-biblioteca-ambrosiana/search?q=' \
              + KEYWORD

Images_are_already_downloaded = False
