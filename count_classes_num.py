def file_name(file_dir, train_txt_path, valid_txt_path, sep_times=2):
    train_f = open(train_txt_path, 'w')
    valid_f = open(valid_txt_path, 'w')
    for root_path, dirs, files in os.walk(file_dir):
        # print(root_path)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
        # random.shuffle(files)
        train_idx_list = []
        valid_idx_list = []
        sep_part = int(np.round(sep_times + 1))
        for idx in range(len(files)):
            if idx % sep_part == 1:
                valid_idx_list.append(idx)
            else:
                train_idx_list.append(idx)

        random.shuffle(train_idx_list)
        random.shuffle(valid_idx_list)
        for train_idx in train_idx_list:
            abs_img_path = os.path.join(root_path, files[train_idx])
            abs_img_path = ''.join((abs_img_path, '\n'))
            train_f.write(abs_img_path)

        for valid_idx in valid_idx_list:
            abs_img_path = os.path.join(root_path, files[valid_idx])
            abs_img_path = ''.join((abs_img_path, '\n'))
            valid_f.write(abs_img_path)
    train_f.close()
    valid_f.close()