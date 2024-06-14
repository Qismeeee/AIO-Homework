def exercise1(tp, fp, fn):
    if not isinstance(tp, int):
        print("tp must be int")
        return
    if not isinstance(fp, int):
        print("fp must be int")
        return
    if not isinstance(fn, int):
        print("fn must be int")
        return

    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp, fp, and fn must be greater than zero")
        return

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = (2 * precision * recall) / (precision + recall)
    print(f'Precision is: {precision}')
    print(f'Recall is: {recall}')
    print(f'F1-score is: {f1_score}')

def main():
    try:
        tp = input("TP is: ")
        if not tp.isdigit():
            print("tp must be int")
            return
        tp = int(tp)

        fp = input("FP is: ")
        if not fp.isdigit():
            print("fp must be int")
            return
        fp = int(fp)

        fn = input("FN is: ")
        if not fn.isdigit():
            print("fn must be int")
            return
        fn = int(fn)

        if tp <= 0 or fp <= 0 or fn <= 0:
            print("tp, fp, and fn must be greater than zero")
            return

        exercise1(tp, fp, fn)

    except ValueError:
        print("Please enter valid integers")

if __name__ == "__main__":
    main()
