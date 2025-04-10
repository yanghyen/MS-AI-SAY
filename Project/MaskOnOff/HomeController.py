from Data.Data import Data


if __name__ == "__main__":
    fluPdfUrl = Data.getFluRatioPdfUrl()
    fluRatio = Data.getFluRatio(fluPdfUrl)
    