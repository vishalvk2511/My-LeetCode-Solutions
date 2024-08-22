/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
    struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* result_Head;
    struct ListNode* temp1 = l1;
    struct ListNode* temp2 = l2;
    struct ListNode* temp = NULL;
    struct ListNode* new;
    int sum, carry;

    result_Head = NULL;

    sum = 0;
    carry = 0;

    while (temp1 || temp2) {
        sum = 0 + carry;

        if (temp1 != NULL) {
            sum += temp1->val;
            temp1 = temp1->next;
        }
        if (temp2 != NULL) {
            sum += temp2->val;
            temp2 = temp2->next;
        }

        carry = sum / 10;
        sum = sum % 10;
        new = (struct ListNode*)malloc(sizeof(struct ListNode));
        new->val = sum;
        new->next = NULL;

        if (result_Head == NULL) {
            result_Head = new;
        } else {
            temp = result_Head;
            if (result_Head != NULL) {
                while (temp->next != NULL) {

                    temp = temp->next;
                }
            }

            temp->next = new;
        }

    }

    if(carry>0){
         new = (struct ListNode*)malloc(sizeof(struct ListNode));
        new->val = carry;
        new->next = NULL;
        temp = result_Head;
            if (result_Head != NULL) {
                while (temp->next != NULL) {

                    temp = temp->next;
                }
            }

            temp->next = new;


    }
    return result_Head;
}
