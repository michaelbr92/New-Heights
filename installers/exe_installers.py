from installers.exe_installer import ExeInstaller
from constants import Apps, DOWNLOADS_DIR

miniconda = Apps.MiniConda.value
seven_zip = Apps.SevenZip.value

seven_zip_installer = ExeInstaller(
                                                        DOWNLOADS_DIR, 
                                                        seven_zip.APP_NAME,
                                                         'version1', 
                                                        seven_zip.URL,  
                                                        seven_zip.INSTALL_COMMAND,
                                                        seven_zip.INSTALLATION_FOLDER
                                                        )

miniconda_installer = ExeInstaller(
                                                        DOWNLOADS_DIR, 
                                                        miniconda.APP_NAME,
                                                         'version1', 
                                                        miniconda.URL,  
                                                        miniconda.INSTALL_COMMAND,
                                                        miniconda.INSTALLATION_FOLDER
                                                        )
