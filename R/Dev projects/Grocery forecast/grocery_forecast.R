```{r grocery.forecast}
coles<-list.files('/Users/d3ops/Library/CloudStorage/GoogleDrive-darren@d3tape.com/Shared drives/Orders/Australia/Coles', pattern = '*.csv', full.names = T)%>%lapply(.,read.csv)%>%do.call(rbind,.)
woolies<-list.files('/Users/d3ops/Library/CloudStorage/GoogleDrive-darren@d3tape.com/Shared drives/Orders/Australia/Woolworths', pattern = '*.csv', full.names = T)%>%lapply(.,read.csv)%>%do.call(rbind,.)

combined<-rbind(coles,woolies)%>%group_by(X.Description)%>%summarise(total_qty = sum(X.Quantity))

week_total<-length(list.files('/Users/d3ops/Library/CloudStorage/GoogleDrive-darren@d3tape.com/Shared drives/Orders/Australia/Woolworths', pattern = '*.csv'))

divider<-function(x){x/week_total}
weekly_demand<-mutate(combined,per_week = round(divider(combined$total_qty),0))
```





#order_dates1<-str_extract((list.files('/Users/d3ops/Library/CloudStorage/GoogleDrive-darren@d3tape.com/Shared drives/Orders/Australia/Coles', pattern = '*.csv', full.names = T)),"[0-9]{4}\\-[0-9]{2}\\-[0-9]{2}")
#order_dates2<-str_extract((list.files('/Users/d3ops/Library/CloudStorage/GoogleDrive-darren@d3tape.com/Shared drives/Orders/Australia/woolworths', pattern = '*.csv', full.names = T)),"[0-9]{4}\\-[0-9]{2}\\-[0-9]{2}")

#paste(order_dates1,order_dates2, collapse = " ")%>%str_split(.," ")%>%lapply(as.Date)

#coles_infolist<-file.info(list.files('/Users/d3ops/Library/CloudStorage/GoogleDrive-darren@d3tape.com/Shared drives/Orders/Australia/Coles', pattern = '*.csv', full.names = T))#woolies_infolist<-file.info(list.files('/Users/d3ops/Library/CloudStorage/GoogleDrive-darren@d3tape.com/Shared drives/Orders/Australia/Woolworths', pattern = '*.csv', full.names = T))
#date_range<-rbind(coles_infolist,woolies_infolist)

#start_date_range<-which.min(date_range$ctime)
#end_date_range<-which.max(date_range$ctime)
