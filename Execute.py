import Extract,Transform,Load
import logging

if __name__ == '__main__':
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    # 1. Run Extract
    logging.info('# 1. Run Extract')
    downloaded_files=Extract.Extract_all()
    print(downloaded_files)
    # 2. Run Transform
    logging.info('# 1. Run Transform')
    Transform.Transform(downloaded_files)
    # 2. Run Transform
    logging.info('# 1. Run Load')
    Load.load(downloaded_files)
