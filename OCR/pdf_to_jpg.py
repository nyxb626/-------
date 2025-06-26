from pdf2image import convert_from_path
import os

# 设置包含子文件夹的根文件夹路径
input_root_folder = '/Users/hansen/Desktop/1-50'  # 替换为你的根文件夹路径
output_root_folder = '/Users/hansen/Desktop/1-50_images'  # 替换为你希望存储图片文件夹的路径

# 如果输出根文件夹不存在，则创建
os.makedirs(output_root_folder, exist_ok=True)

# 遍历根文件夹中的所有子文件夹
for subfolder in os.listdir(input_root_folder):
    subfolder_path = os.path.join(input_root_folder, subfolder)
    
    # 检查是否为文件夹
    if os.path.isdir(subfolder_path):
        # 遍历子文件夹中的所有PDF文件
        for pdf_file in os.listdir(subfolder_path):
            if pdf_file.endswith('.pdf'):  # 只处理PDF文件
                pdf_path = os.path.join(subfolder_path, pdf_file)
                
                # 创建与子文件夹对应的输出文件夹
                output_subfolder = os.path.join(output_root_folder, subfolder)
                os.makedirs(output_subfolder, exist_ok=True)
                
                # 创建以PDF文件名命名的输出文件夹（去除扩展名）
                pdf_name = os.path.splitext(pdf_file)[0]
                output_folder = os.path.join(output_subfolder, pdf_name)
                os.makedirs(output_folder, exist_ok=True)
                
                # 转换PDF为图片
                print(f"正在处理文件：{pdf_file} (位于 {subfolder})")
                images = convert_from_path(pdf_path, dpi=300)  # dpi可以调整以改变图片质量
                
                # 保存每一页为一张图片
                for i, image in enumerate(images):
                    image_path = os.path.join(output_folder, f'page_{i+1}.jpg')
                    image.save(image_path, 'JPEG')
                
                print(f"文件 {pdf_file} 已转换为图片，并保存在文件夹：{output_folder}")

print(f"所有PDF文件已处理完成，图片保存在：{output_root_folder}")
