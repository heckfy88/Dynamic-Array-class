import ctypes


class DynamicArray(object):
    """
    Dynamic array class
    """

    def __init__(self):
        self.n = 0  # Number of actual elements (default is set to 0)
        self.capacity = 1  # Default capacity (set to 1)
        self.Array = self.make_array(self.capacity)

    def __len__(self):
        """
        Returns the number of elements sorted in array
        """
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError("the element with index {} is out of bounds".format(k))  # Check if the element with k index is in array
        return self.Array[k]  # Return the element of an array with k index

    def append(self, element):
        """
        Adds an element at the end of an array
        """
        if self.n == self.capacity:
            self._resize(2 * self.capacity)  # If the number of elements is equal to the capacity - double the capacity

        self.Array[self.n] = element  # Set self.n index to the element
        self.n += 1  # As the self.Array[self.n] is filled with element, place the counter on the next cell

    def _resize(self, new_capacity):
        """
        Resizes the internal array to a new capacity
        """
        buffer_array = self.make_array(new_capacity)  # New bigger array for buffer

        for k in range(self.n):  # Reference all existing values
            buffer_array[k] = self.Array[k]

        self.Array = buffer_array  # Assign all values back to initial array
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        """
        Returns new array with new_capacity capacity
        """
        return (new_capacity * ctypes.py_object)()




