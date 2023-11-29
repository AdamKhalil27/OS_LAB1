#include <linux/module.h> // Include for all kernel modules
#include <linux/kernel.h> // Include for kernel's printk function

int init_module(void)
{
    printk(KERN_INFO "Hello, World!\n");
    return 0; // Successful return indicates successful module loading.
}

void cleanup_module(void)
{
    printk(KERN_INFO "Goodbye, World!\n");
}

obj-m += hello_world.o

all:
    make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
    make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean

#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>

static int param = 0;

module_param(param, int, S_IRUSR | S_IWUSR);
MODULE_PARM_DESC(param, "An integer parameter");

static int __init example_init(void)
{
    printk(KERN_INFO "Module loaded with parameter: %d\n", param);
    return 0;
}

static void __exit example_exit(void)
{
    printk(KERN_INFO "Module unloaded\n");
}

module_init(example_init);
module_exit(example_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Your Name");
MODULE_DESCRIPTION("A simple example with module parameters");
