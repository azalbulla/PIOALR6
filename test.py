from avltree import AVLTree
from rbtree import RBTree


def main():
    print("АВЛ и Красно-черные деревья")

    print("\n1. АВЛ-Дерево (ключи: 4, 5, 7, 2, 1, 3, 6)")

    avl = AVLTree()
    root = None
    keys = [4, 5, 7, 2, 1, 3, 6]

    for key in keys:
        root = avl.insert(root, key)
        print(f"Вставлено {key}, Корень={root.key}, Высота={root.height}")

    print("\nСтруктура AVL дерева:")
    avl.print_tree(root)

    print(f"\nIn-order обход: {avl.inorder(root)}")
    print(f"Высота дерева: {avl.get_height(root)}")
    print(f"Баланс корня: {avl.get_balance(root)}")

    search_key = 3
    res = avl.search(root, search_key)
    print(f"\nПоиск ключа {search_key}: {'Найден' if res else 'Не найден'}")

    print("\nУдаление ключа 7")
    root = avl.delete(root, 7)
    print(f"In-order после удаления: {avl.inorder(root)}")
    print("\nДерево после удаления:")
    avl.print_tree(root)

    print("\n2. Красно-Чёрное Дерево (ключи: 10, 20, 30, 15, 25, 5, 1)")

    rb = RBTree()
    rb_keys = [10, 20, 30, 15, 25, 5, 1]

    for key in rb_keys:
        rb.insert(key)
        print(f"Вставлено {key}")

    print("\nСтруктура Красно-Чёрного дерева:")
    rb.print_tree()
    print(f"\nIn-order обход: {rb.inorder()}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Ошибка: {e}")
