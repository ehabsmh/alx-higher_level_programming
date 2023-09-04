#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if there's a cycle in a linked list
 * @list: head of linked list
 *
 * Return: 0 if there's no cycle
 * Otherwise return 1
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
