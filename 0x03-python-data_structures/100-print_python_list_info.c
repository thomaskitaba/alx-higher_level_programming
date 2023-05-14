#include <stdio.h>
#include <Python.h>
/**
* print_python_list_info - print basic list info
* @p: pointer to a pythonlistobject
* Return: nothing
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t length, i;
	char *typeName;
	PyObject *item;
	/* to iteraate*/
	length = PyList_Size(p);
	for (i = 0; i < length; i++)
	{
		item = PyList_GetItem(p, i);
		printf("index %Zd:  %s\n", i, Py_TYPE(item)->tp_name));
	}
	/*once we get size or length of the list we can traverse it*/
}
