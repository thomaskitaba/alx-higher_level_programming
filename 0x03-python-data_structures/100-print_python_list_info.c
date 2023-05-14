#include <stdio.h>
#include <Python.h>
/**
* print_python_list_info - print basic list info
* @p: pointer to a pythonlistobject
* Return: nothing
*/
void print_python_list_info(PyObject *p)
{
	int len, allocatedated, i;
	PyObject *obj;

	length = Py_length(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] length of the Python List = %d\n", length);
	printf("[*] allocatedated = %d\n", allocated);

	for (i = 0; i < length; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}

	/*once we get length or length of the list we can traverse it*/
}
