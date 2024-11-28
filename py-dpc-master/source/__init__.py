"""
用Python做的各种工具，放在模块之中直接调用
"""
import sys


from .__version__ import (
    __title__,
    __description__,
    __url__,
    __author__,
    __author_email__,
)

# 在Windows系统下，导入相关模块
if sys.platform.startswith('win'):
    from .OCR import (
        character_recognition,
    )

    from .OfficeOperation import (
        get_xlsx_column_data,
    )

from .Account import (
    input_password,
    change_password,
)

from .Data import (
    list_count,
    list_sort
)

from .Math import (
    get_fibonacci,
    fibonacci_sequence,
)

from .FileOperation import (
    read_file_to_list,
    save_list_to_file,
    get_file_name_from_folder,
    get_file_full_name_from_folder,
    get_file_and_folder_full_name_from_folder,
)

from .Database import (
    create_table,
    add_data,
    modify_data,
    delete_data_by_ID,
    read_data_to_list,
    read_column_data_to_list,
)


from .Console import (
    menu_display,
    clear_screen,
)

from .Logger import (
    logger_config,
)

from .PackageManager import (
    upgrade_package,
)
