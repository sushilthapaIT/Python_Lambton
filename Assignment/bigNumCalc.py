class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, element):
        new_node = Node(element)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def addLast(self, element):
        new_node = Node(element)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            raise Exception("List is empty")
        else:
            removed = self.head
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1
            return removed.data

    def removeLast(self):
        if self.isEmpty():
            raise Exception("List is empty")
        else:
            removed = self.tail
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.size -= 1
            return removed.data

    def add(self, element, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        elif index == 0:
            self.addFirst(element)
        elif index == self.size:
            self.addLast(element)
        else:
            new_node = Node(element)
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node
            self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        elif index == 0:
            return self.removeFirst()
        elif index == self.size - 1:
            return self.removeLast()
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1
            return current.data

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return '\n'.join(map(str, result))

    def __eq__(self, other):
        if self.size != other.size:
            return False
        current_self = self.head
        current_other = other.head
        while current_self:
            if current_self.data != current_other.data:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return True

    def __add__(self, other):
        result = DoublyLinkedList()
        current_self = self.head
        current_other = other.head
        carry = 0
        while current_self or current_other:
            if current_self:
                val_self = current_self.data
                current_self = current_self.next
            else:
                val_self = 0
            if current_other:
                val_other = current_other.data
                current_other = current_other.next
            else:
                val_other = 0
            sum_val = val_self + val_other + carry
            result.addLast(sum_val % 10)
            carry = sum_val // 10
        if carry > 0:
            result.addLast(carry)
        return result

    def __len__(self):
        return self.size


class bigNum:
    def __init__(self, value='0'):
        self.digits = DoublyLinkedList()
        if value[0] == '-':
            self.sign = '-'
            value = value[1:]
        else:
            self.sign = '+'
        for char in reversed(value):
            self.digits.addLast(int(char))

    def __str__(self):
        if self.sign == '-':
            return '-' + str(self.digits)
        else:
            return str(self.digits)

    def __eq__(self, other):
        return self.sign == other.sign and self.digits == other.digits

    def __gt__(self, other):
        if self.sign == '+' and other.sign == '-':
            return True
        elif self.sign == '-' and other.sign == '+':
            return False
        elif len(self.digits) > len(other.digits):
            return self.sign == '+'
        elif len(self.digits) < len(other.digits):
            return self.sign == '-'
        else:
            current_self = self.digits.head
            current_other = other.digits.head
            while current_self:
                if current_self.data > current_other.data:
                    return self.sign == '+'
                elif current_self.data < current_other.data:
                    return self.sign == '-'
                current_self = current_self.next
                current_other = current_other.next
        return False

    def __lt__(self, other):
        return not (self == other or self > other)

    def __add__(self, other):
        if self.sign == other.sign:
            result = bigNum()
            carry = 0
            current_self = self.digits.head
            current_other = other.digits.head
            while current_self or current_other:
                if current_self:
                    val_self = current_self.data
                    current_self = current_self.next
                else:
                    val_self = 0
                if current_other:
                    val_other = current_other.data
                    current_other = current_other.next
                else:
                    val_other = 0
                sum_val = val_self + val_other + carry
                result.digits.addLast(sum_val % 10)
                carry = sum_val // 10
            if carry > 0:
                result.digits.addLast(carry)
            result.sign = self.sign
            return result
        else:
            return self.__sub__(bigNum(other.sign + str(other.digits)))

    def __sub__(self, other):
        if self.sign != other.sign:
            result = self.__add__(bigNum(other.sign + str(other.digits)))
            result.sign = self.sign
            return result
        elif self == other:
            return bigNum('0')
        elif self > other:
            result = bigNum()
            borrow = 0
            current_self = self.digits.head
            current_other = other.digits.head
            while current_self or current_other:
                if current_self:
                    val_self = current_self.data
                    current_self = current_self.next
                else:
                    val_self = 0
                if current_other:
                    val_other = current_other.data
                    current_other = current_other.next
                else:
                    val_other = 0
                diff_val = val_self - val_other - borrow
                if diff_val < 0:
                    diff_val += 10
                    borrow = 1
                else:
                    borrow = 0
                result.digits.addLast(diff_val)
            result.sign = self.sign
            return result
        else:
            result = other.__sub__(self)
            result.sign = '-' if self.sign == '+' else '+'
            return result

    def __mul__(self, other):
        result = bigNum()
        current_self = self.digits.head
        position_self = 0
        while current_self:
            current_other = other.digits.head
            carry = 0
            result_temp = bigNum()
            for _ in range(position_self):
                result_temp.digits.addLast(0)
            while current_other:
                prod_val = current_self.data * current_other.data + carry
                result_temp.digits.addLast(prod_val % 10)
                carry = prod_val // 10
                current_other = current_other.next
            if carry > 0:
                result_temp.digits.addLast(carry)
            result = result + result_temp
            current_self = current_self.next
            position_self += 1
        result.sign = '-' if self.sign != other.sign else '+'
        return result

    def __div__(self, other):
        quotient = bigNum()
        dividend = bigNum(str(self))
        divisor = bigNum(str(other))
        while dividend >= divisor:
            temp_divisor = divisor
            temp_quotient = bigNum('1')
            while dividend >= temp_divisor:
                dividend = dividend - temp_divisor
                quotient = quotient + temp_quotient
                temp_divisor = temp_divisor + temp_divisor
                temp_quotient = temp_quotient + temp_quotient
        quotient.sign = '-' if self.sign != other.sign else '+'
        return quotient

    def __len__(self):
        return len(self.digits)


def main():
    with open('bigNums.txt', 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines if line.strip()]  # Remove empty lines and leading/trailing whitespace
    print("******************")
    print("BigNum Calculator")
    print("******************")
    result = bigNum(lines[0])  # No need to call strip() here
    print(f"{result}")
    for i in range(1, len(lines), 2):
        operand = lines[i]
        operand_value = bigNum(lines[i + 1])  # No need to call strip() here
        print(f"{result} {operand} {operand_value} = ", end="")
        if operand == '+':
            result = result + operand_value
        elif operand == '-':
            result = result - operand_value
        elif operand == '*':
            result = result * operand_value
        elif operand == '/':
            result = result / operand_value
        print(f"{result}")
    print("******************")
    print("Final result")
    print("******************")
    print(f"{result}")


if __name__ == "__main__":
    main()
