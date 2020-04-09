import json

def main():
     dates = ["2020-03-25@21-45",
              "2020-03-26@12-45",
              "2020-03-26@18-04",
              "2020-03-27@09-49",
              "2020-03-27@18-09",
              "2020-03-28@09-44",
              "2020-03-29@18-28",
              "2020-03-30@09-27",
              "2020-03-31@10-06",
              "2020-03-31@19-18",
              "2020-04-01@17-51",
              "2020-04-02@19-49",
              "2020-04-03@10-38",
              "2020-04-04@09-15",
              "2020-04-06@21-40",
              "2020-04-08@21-04",
              "2020-04-09@12-21",]
     
     
     # get all time data into array
     all_time = {}
     for date in dates:
         filename = 'covid_' + date + '.json'
         with open(filename) as f:
             daily = json.load(f)
     
         key = ("%s" % date)
         all_time[key] = daily

     # transpose the data into desired format
     transposed = []
     for region_name in all_time["2020-04-09@12-21"].keys():
         data = []
         for date in dates:
             for key in all_time[date].keys():
                 if key == region_name:
                     data.append({
                         'date': date,
                         'value': all_time[date][key]
                     })

         transposed.append({
             "name": region_name,
             "data": data         
         })

     print(json.dumps(transposed,indent=4, sort_keys=True, ensure_ascii=False))



if (__name__ == "__main__"):
    main()
