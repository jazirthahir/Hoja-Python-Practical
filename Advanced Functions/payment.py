def payment(total,gst,coupon): #total to sub coupon , total add gst
    result = total + gst - coupon
    return result

total = 100
gst = 18
coupon = 40

grand_total = payment(total,gst,coupon)
print(grand_total)