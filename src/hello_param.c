#define pr_fmt(fmt) KBUILD_MODNAME ": " fmt

#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/moduleparam.h>
#include <linux/stat.h>

#define MAX_ARRAY_LEN 10  // Разрешим до 10 элементов

static short int myshort = 1;
static int myint = 420;
static long int mylong = 9999;
static char *mystring = "OTUS";
static int myintarray[MAX_ARRAY_LEN] = {420, 420};
static int arr_argc = 2;  // Установим соответствие значению по умолчанию

module_param(myshort, short, S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP);
MODULE_PARM_DESC(myshort, "A short integer");

module_param(myint, int, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);
MODULE_PARM_DESC(myint, "An integer");

module_param(mylong, long, S_IRUSR);
MODULE_PARM_DESC(mylong, "A long integer");

module_param(mystring, charp, S_IRUGO);
MODULE_PARM_DESC(mystring, "A character string");

module_param_array(myintarray, int, &arr_argc, S_IRUSR | S_IWUSR);
MODULE_PARM_DESC(myintarray, "An array of integers (max " __stringify(MAX_ARRAY_LEN) ")");

static int __init hello_param_init(void)
{
	int i;

	pr_info("Hello, World from the kernel!\n");

	pr_info("myshort = %hd\n", myshort);
	pr_info("myint = %d\n", myint);
	pr_info("mylong = %ld\n", mylong);
	pr_info("mystring = %s\n", mystring);

	if (arr_argc > MAX_ARRAY_LEN) {
		pr_warn("Only first %d elements of myintarray will be used (received %d).\n", MAX_ARRAY_LEN, arr_argc);
		arr_argc = MAX_ARRAY_LEN;
	}

	for (i = 0; i < arr_argc; i++)
		pr_info("myintarray[%d] = %d\n", i, myintarray[i]);

	pr_info("Total valid arguments for myintarray: %d\n", arr_argc);

	return 0;
}

static void __exit hello_param_exit(void)
{
	pr_info("Goodbye, World from the kernel!\n");
}

module_init(hello_param_init);
module_exit(hello_param_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("otusru");
MODULE_DESCRIPTION("A simple Hello Param module for the Linux kernel");
