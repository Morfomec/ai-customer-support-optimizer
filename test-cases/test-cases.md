# Test Cases

## Purpose

These test cases will be used to test the AI customer support workflow.

The same test cases will be used for both the baseline prompt and the optimized prompt so that the results can be compared fairly.

---

## TC01 — Duplicate Payment

### Customer Message

I was charged ₹500 twice for my subscription. Please refund the extra payment.

### Expected Behavior

The AI should:

* Acknowledge the duplicate payment.
* Show empathy.
* Explain the appropriate next step.
* Avoid claiming that a refund has already been processed.
* Avoid inventing a refund timeline.

---

## TC02 — Delayed Order

### Customer Message

My order hasn't arrived yet. It was supposed to arrive yesterday.

### Expected Behavior

The AI should:

* Acknowledge the delivery delay.
* Show empathy.
* Explain what the customer should do next.
* Avoid claiming that it checked the order.
* Avoid inventing an order status or delivery date.

---

## TC03 — Forgot Password

### Customer Message

I forgot my password and cannot log into my account.

### Expected Behavior

The AI should:

* Understand that the customer needs help accessing their account.
* Provide a clear password-reset step.
* Keep the response simple.
* Avoid asking for unnecessary information.

---

## TC04 — Refund Policy

### Customer Message

I want to cancel my subscription. Will I get my money back?

### Expected Behavior

The AI should:

* Explain that refund eligibility depends on the company's refund policy.
* Avoid inventing a refund policy.
* Avoid saying that the customer definitely will or will not receive a refund when the policy is not provided.
* Tell the customer what information or next step is needed.

---

## TC05 — Angry Customer

### Customer Message

Your service is terrible. I've been waiting three days for someone to help me!

### Expected Behavior

The AI should:

* Acknowledge the customer's frustration.
* Use a calm and empathetic tone.
* Address the customer's concern.
* Provide a useful next step.
* Avoid making promises that are not supported by the available information.
