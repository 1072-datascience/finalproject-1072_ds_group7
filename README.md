# <AI Cup 生醫論文自動分析-生醫關聯擷取 >

### Groups
* < 賴彥儒, 105701027 >
* < 林煜翰, 105701037 >
* < 廖禾豪, 106703045 >
* < 黃郁軒, 106703049 >

### Goal
根據文獻內容判斷兩個指定基因間的關係為哪一種類型

### Demo 
You should provide an example commend to reproduce your result
```R
Rscript code/your_script.R --input data/training --output results/performance.tsv
```
* any on-line visualization

## Folder organization and its related information

### docs
* Your presentation, 1072_datascience_FP_<yourID|groupName>.ppt/pptx/pdf, by **Jun. 25**
* Any related document for the final project
  * papers
  * software user guide

### data

* Source: AI Cup 比賽網站(https://aidea-web.tw/topic/d0cec130-b15d-4c4c-b7e8-bf95a0c34dd8)
* Input format: .tsv
* Preprocessing:
  * Natural Language ToolKit
  * 針對 Gene.Gene_ID 及 Gene_Index.start.end Separate “ | ”, 使兩行資料各自分開顯示其name, ID, Start, End, Length 


### code

* Method do you use: SVM
* Null model for comparison: Random Forests
* Perform evaluation: Cross-validation

### results

* Which metric do you use: precision
* Is your improvement significant? : )
* What is the challenge part of your project? 
   將sentence數據化並可以被歸類、建模真的好難orz

## Reference
* Code/implementation which you include/reference (__You should indicate in your presentation if you use code for others. Otherwise, cheating will result in 0 score for final project.__)
* Packages you use
* Related publications


