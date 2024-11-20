# import tkinter as tk
from tkinter import filedialog as fd
# import openpyxl


def main():

    wb = fd.askopenfile(mode='r')
    header = wb.readline(0)
    print(header)

class ProductData:
    def __init__(self, gtin, full_name, brand, sub_brand, functional_name,
                 color, variant, presentation, category, size, roll_width,
                 roll_length, sku, udi_di, is_active, inner_sku, inner_gtin,
                 shipper_sku, shipper_gtin, manufacturer_sku, harmonised_tariff,
                 gpc_code, base_width, base_depth, base_height, inner_width,
                 inner_depth, inner_height, shipper_width, shipper_depth,
                 shipper_height, net_weight, gross_weight, inner_weight,
                 shipper_weight, units_per_inner, inners_per_shipper,
                 shippers_per_pallet_level, pallet_levels_per_pallet):
        
        self.gtin = gtin
        self.full_name = full_name
        self.brand = brand
        self.sub_brand = sub_brand
        self.functional_name = functional_name
        self.color = color
        self.variant = variant
        self.presentation = presentation
        self.category = category
        self.size = size
        self.roll_width = roll_width
        self.roll_length = roll_length
        self.sku = sku
        self.udi_di = udi_di
        self.is_active = is_active
        self.inner_sku = inner_sku
        self.inner_gtin = inner_gtin
        self.shipper_sku = shipper_sku
        self.shipper_gtin = shipper_gtin
        self.manufacturer_sku = manufacturer_sku
        self.harmonised_tariff = harmonised_tariff
        self.gpc_code = gpc_code
        self.base_width = base_width
        self.base_depth = base_depth
        self.base_height = base_height
        self.inner_width = inner_width
        self.inner_depth = inner_depth
        self.inner_height = inner_height
        self.shipper_width = shipper_width
        self.shipper_depth = shipper_depth
        self.shipper_height = shipper_height
        self.net_weight = net_weight
        self.gross_weight = gross_weight
        self.inner_weight = inner_weight
        self.shipper_weight = shipper_weight
        self.units_per_inner = units_per_inner
        self.inners_per_shipper = inners_per_shipper
        self.shippers_per_pallet_level = shippers_per_pallet_level
        self.pallet_levels_per_pallet = pallet_levels_per_pallet

# for product in range(len(wb)):
#     gtin = 



if __name__ == "__main__":
    main()
