db.messages.findOne({ "headers.Message-ID": "<8147308.1075851042335.JavaMail.evans@thyme>" })

db.messages.update(
{ "headers.Message-ID": "<8147308.1075851042335.JavaMail.evans@thyme>" },
{ $push : { "headers.To" : "mrpotatohead@10gen.com" } })