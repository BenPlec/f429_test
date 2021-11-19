import os
import struct
import binascii
# from PIL import Image
file_name = 'plecko5'
curr_dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = curr_dir_path + '/userlib_pic/{0}.bmp'.format(file_name)

bmp = open(file_path, "rb")
# print(bmp)

def Byte4_Conversion(filepath_info):
    str_tmp = struct.unpack('I', filepath_info.read(4))
    num_tmp = int(str_tmp[0])
    hex_tmp = hex(num_tmp)
    hex_wo_0x = hex_tmp[2:len(hex_tmp)]
    hex_le = []
    for i in range(len(hex_wo_0x), 0, -2):
        if i == 1: # Exception for odd number
            tt = '0%s' % hex_wo_0x[i-1]
            hex_le.append(tt)
        else:
            tt = ''.join(hex_wo_0x[i-2:i])
            hex_le.append(tt)

    if len(hex_le) < 4:
        for i in range(0, 4-len(hex_le)):
            hex_le.append('00')
    return '0x{0}, 0x{1}, 0x{2}, 0x{3}, '.format(hex_le[0], hex_le[1], hex_le[2], hex_le[3])

def Byte2_Conversion(filepath_info):
    str_tmp = struct.unpack('H', filepath_info.read(2))
    num_tmp = int(str_tmp[0])
    hex_tmp = hex(num_tmp)
    hex_wo_0x = hex_tmp[2:len(hex_tmp)]
    hex_le = []
    for i in range(len(hex_wo_0x), 0, -2):
        if i == 1: # Exception for odd number
            tt = '0%s' % hex_wo_0x[i-1]
            hex_le.append(tt)
        else:
            tt = ''.join(hex_wo_0x[i-2:i])
            hex_le.append(tt)

    if len(hex_le) < 2:
        for i in range(0, 2-len(hex_le)):
            hex_le.append('00')
    return '0x{0}, 0x{1}, '.format(hex_le[0], hex_le[1])

# # # # # # # # # # # # # # # # # # # #
# Bitmap file header
# bfType[2], bfSize[4], bfReserved1[2], bfReserved2[2], bfOffBits[4]

# bfType: 2 Bytes, BM Character
print('Type:', bmp.read(2).decode())
bfType = '0x42, 0x4D, '

# bfSize: 4 Bytes, File size
# print('Size: %s' % struct.unpack('I', bmp.read(4)))
bfSize = Byte4_Conversion(bmp)
print('Size: ', bfSize)

# bfReserved1 and bfReserved2: 2 Bytes
print('Reserved 1: %s' % struct.unpack('H', bmp.read(2)))
bfReserved1 = "0x00, 0x00, "
print('Reserved 2: %s' % struct.unpack('H', bmp.read(2)))
bfReserved2 = "0x00, 0x00, "

# bfOffBits: 4 Bytes, Start position
# print('Offset: %s' % struct.unpack('I', bmp.read(4)))
bfOffBits = Byte4_Conversion(bmp)
print('Offset: ', bfOffBits)

# # # # # # # # # # # # # # # # # # # #
# Bitmap Information header
# biSize[4], biWidth[4], biHeight[4], biPlanes[2], biBitCount[2],
# biCompression[4], biSizeImage[4], biXPelsPerMeter[4], biYPelsPerMeter[4]
# biClrUsed [4], biClrImportant[4]

# biSize[4]: Bitmap information header size
# print('DIB Header Size: %s' % struct.unpack('I', bmp.read(4)))
biSize = Byte4_Conversion(bmp)
print('DIB Header Size: ', biSize)

# biWidth[4]: Bitmap image width in pixel
# print('Width: %s' % struct.unpack('I', bmp.read(4)))
biWidth = Byte4_Conversion(bmp)
print('Width: ', biWidth)

# biHeight[4]: Bitmap image height in pixel
# print('Height: %s' % struct.unpack('I', bmp.read(4)))
biHeight = Byte4_Conversion(bmp)
print('Height: ', biHeight)

# biPlanes[2]: Bitmap color plane, must be 1
# print('Colour Planes: %s' % struct.unpack('H', bmp.read(2)))
biPlanes = Byte2_Conversion(bmp)
print('Colour Planes: ', biPlanes)

# biBitCount[2]: Bits per Pixel
# print('Bits per Pixel: %s' % struct.unpack('H', bmp.read(2)))
    # str_tmp = struct.unpack('H', bmp.read(2))
    # # num_tmp = int(str_tmp[0])
    # num_tmp = 16
    # hex_tmp = hex(num_tmp)
    # hex_wo_0x = hex_tmp[2:len(hex_tmp)]
    # hex_le = []
    # for i in range(len(hex_wo_0x), 0, -2):
    #     if i == 1: # Exception for odd number
    #         tt = '0%s' % hex_wo_0x[i-1]
    #         hex_le.append(tt)
    #     else:
    #         tt = ''.join(hex_wo_0x[i-2:i])
    #         hex_le.append(tt)

    # if len(hex_le) < 2:
    #     for i in range(0, 2-len(hex_le)):
    #         hex_le.append('00')
    # biBitCount = '0x{0}, 0x{1}, '.format(hex_le[0], hex_le[1])
biBitCount = Byte2_Conversion(bmp)
print('Bits per Pixel: ', biBitCount)

# biCompression[4]: Compression method, usually 0
# print('Compression Method: %s' % struct.unpack('I', bmp.read(4)))
biCompression = Byte4_Conversion(bmp)
print('Compression Method: ', biCompression)

# biSizeImage[4]: Bitmap image pixel data size
# print('Raw Image Size: %s' % struct.unpack('I', bmp.read(4)))
biSizeImage = Byte4_Conversion(bmp)
print('Raw Image Size: ', biSizeImage)

# biXPelsPerMeter[4]: Horizontal resolution in pixel per meter
# print('Horizontal Resolution: %s' % struct.unpack('I', bmp.read(4)))
biXPelsPerMeter = Byte4_Conversion(bmp)
print('Horizontal Resolution: ', biXPelsPerMeter)

# biYPelsPerMeter[4]: Vertical resolution in pixel per meter
# print('Vertical Resolution: %s' % struct.unpack('I', bmp.read(4)))
biYPelsPerMeter = Byte4_Conversion(bmp)
print('Vertical Resolution: ', biYPelsPerMeter)

# biClrUsed [4]: Number of colors in the Palette
# print('Number of Colours: %s' % struct.unpack('I', bmp.read(4)))
biClrUsed = Byte4_Conversion(bmp)
print('Number of Colours: ', biClrUsed)

# biClrImportant[4]: Number of required color index
# print('Important Colours: %s' % struct.unpack('I', bmp.read(4)))
biClrImportant = Byte4_Conversion(bmp)
print('Important Colours: ', biClrImportant)

FileHeader = ''
FileHeader += bfType
FileHeader += bfSize
FileHeader += bfReserved1
FileHeader += bfReserved2
FileHeader += bfOffBits

InfoHeader = ''
InfoHeader += biSize
InfoHeader += biWidth
InfoHeader += biHeight
InfoHeader += biPlanes
InfoHeader += biBitCount
InfoHeader += biCompression
InfoHeader += biSizeImage
InfoHeader += biXPelsPerMeter
InfoHeader += biYPelsPerMeter
InfoHeader += biClrUsed
InfoHeader += biClrImportant

# print('BITMAPFILEHEADER: ', FileHeader)
# print('BITMAPINFOHEADER: ', InfoHeader)
# print('header file: ', FileHeader + InfoHeader)


# # # # # # # # # # # # # # # # # # # #
# Bitmap Data
biSizeImage_str = []
for i in range(len(biSizeImage) - 1, 0, -6):
    # print(i)
    # print(biSizeImage[i-3:i-1])
    # tt = ''.join(biSizeImage[i-3:i-1])
    biSizeImage_str.append(biSizeImage[i-3:i-1])

biSizeImage_int = int(''.join(biSizeImage_str), 16)
Data_size = int(biSizeImage_int/2)
# print(biSizeImage_int)
# print(Data_size)

BitmapData = ''
for i in range(0, Data_size):
    tt = Byte2_Conversion(bmp)   
    
    if i % 10000 == 1:
        print(tt)
        
    BitmapData += tt
    
    if i % 20 == 19:
        BitmapData += '\n'
# print(BitmapData)


file_path = curr_dir_path + '/user_results/user_picture.h'
with open(file_path, 'w') as headerFile:
    headerFile.write("/* H-file generated by Ben Kim */\n")
    headerFile.write("/* Define to prevent recursive inclusion -------------------------------------*/\n")
    headerFile.write("#ifndef __STM32F429I_DISCOVERY_USER_DEFINE_H\n")
    headerFile.write("#define __STM32F429I_DISCOVERY_USER_DEFINE_H\r\n")
    headerFile.write("__ALIGN_BEGIN const uint8_t {0}".format(file_name))
    headerFile.write('[%d] __ALIGN_END ={\n' % (int(biSizeImage_int + 55)))                     
    headerFile.write("// bmp file header\n")
    headerFile.write(FileHeader)
    headerFile.write("\n")
    headerFile.write("// bmp info header\n")
    headerFile.write(InfoHeader)
    headerFile.write("\n")
    headerFile.write("// bmp data\n")
    headerFile.write(BitmapData)
    headerFile.write("\n")
    headerFile.write("};")
    headerFile.write("\n")
    headerFile.write("#endif /* __STM32F429I_DISCOVERY_USER_DEFINE_H */")
    # headerFile.write(rerere)
    
print("Finished")
    


    
    


