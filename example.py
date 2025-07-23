import json
import lzma
import base64

def decompress_matrix(b64_string):
        compressed_bytes = base64.b64decode(b64_string)
        matrix_bytes = lzma.decompress(compressed_bytes)
        matrix_str = matrix_bytes.decode('utf-8')
        original_list = json.loads(matrix_str)
        # original list is a 1D list containig packed RGB values.
        return original_list

with open("sample_input.txt", "r") as file:
    compressed_lzma = file.read()
packed_rgb = decompress_matrix(compressed_lzma)
print(f"The function gives a list of containing {len(packed_rgb)} elements. These are packed rgb values.\nAll the best\n ~ LaserHammer")
