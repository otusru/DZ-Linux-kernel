#define pr_fmt(fmt) KBUILD_MODNAME ": " fmt

#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/stat.h>
#include <linux/param.h>

static int my_param = 0;

static int param_get(char *buffer, const struct kernel_param *kp)
{
	const int *p = (const int *)kp->arg;
	return scnprintf(buffer, PAGE_SIZE, "%d\n", *p);
}

static int param_set(const char *val, const struct kernel_param *kp)
{
	int res, _val;
	int *p = (int *)kp->arg;

	res = kstrtoint(val, 10, &_val);
	if (res) {
		pr_err("Ошибка: неверное значение параметра!\n");
		return res;
	}

	if (_val < 0 || _val > 100) {
		pr_err("Ошибка: значение должно быть в диапазоне 0–100!\n");
		return -EINVAL;
	}

	*p = _val;
	pr_info("Параметр изменён на: %d\n", *p);
	return 0;
}

static const struct kernel_param_ops param_ops = {
	.set = param_set,
	.get = param_get,
};

module_param_cb(param, &param_ops, &my_param, 0644);
MODULE_PARM_DESC(param, "Пример параметра с callback (диапазон: 0–100)");

static int __init mod_init(void)
{
	pr_info("Модуль загружен. Значение параметра: %d\n", my_param);
	return 0;
}

static void __exit mod_exit(void)
{
	pr_info("Модуль выгружен\n");
}

module_init(mod_init);
module_exit(mod_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("otusru");
MODULE_DESCRIPTION("Модуль ядра с параметром и колбэками get/set");
