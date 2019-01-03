import os
import cv2


def splitter(root):
    new_f = 'classed_data_/'
    count, count_test, count_train, count_val = 0, 0, 0, 0
    folders = os.listdir(root)
    for i in folders:
        if not os.path.exists(new_f + 'train/' + i + '/'):
            os.makedirs(new_f + 'train/' + i + '/')
        if not os.path.exists(new_f + 'val/' + i + '/'):
            os.makedirs(new_f + 'val/' + i + '/')
        if not os.path.exists(new_f + 'test/' + i + '/'):
            os.makedirs(new_f + 'test/' + i + '/')
        total = len(os.listdir(root + i))
        train_am, val_am = total * 0.9, total * 0.85
        for file in os.listdir(root + i):
            img = cv2.imread(root + i + '/' + file)
            if count <= train_am:
                count_train += 1
                cv2.imwrite(new_f + 'train/' + i + '/' + file, img)
            elif count > train_am:
                count_val += 1
                cv2.imwrite(new_f + 'val/' + i + '/' + file, img)
            else:
                count_test += 1
            # cv2.imwrite(new_f+'test/'+i+'/'+file,img)
            count += 1
        print(i, count, count_train, count_val, count_test)
        count, count_test, count_train, count_val = 0, 0, 0, 0


splitter('classed_data/')
