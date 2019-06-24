# <AI Cup 生醫論文自動分析-生醫關聯擷取 >

### Groups
* < 賴彥儒, 105701027 >
* < 林煜翰, 105701037 >
* < 廖禾豪, 106703045 >
* < 黃郁軒, 106703049 >

### Goal
從 PubMed 的生物醫學文獻摘要中辨識和提取具有蛋白質交互作用（Protein-protein Interaction，PPI）資訊之描述句子，
並針對所擷取出來具有 PPI 的句子進行評估，確認兩個指定基因間的關聯性類型

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

* Source: AI Cup 比賽網站 ( https://aidea-web.tw/topic/d0cec130-b15d-4c4c-b7e8-bf95a0c34dd8 )
* Input format: .tsv
    ![input format](/picture/input_format.png)
    
* Preprocessing:
  * Natural Language ToolKit - 把sentence進行分句, 分詞
  * 針對 Gene.Gene_ID 及 Gene_Index.start.end Separate “ | ”, 使兩行資料各自分開顯示其name, ID, Start, End, Length 


### code

* Method do you use:
    * word2vec, SVM, KNN
* Null model for comparison:
    * Random Forests
* Perform evaluation:
    * Cross-validation

### results

* Which metric do you use:
    * precision
* Is your improvement significant? Not Good Enough
* What is the challenge part of your project? 
   * 最大的難題是將sentence套入合適的語料庫並進行分析

## Reference
* Code/implementation which you include/reference 
   * Jiazhi Guo, 2018, accessed 24 June 2019
      * https://www.kaggle.com/jerrykuo7727/word2vec 
   * Youngmi huang, 16 June 2017, accessed 24 June 2019
      * https://medium.com/pyladies-taiwan/%E8%87%AA%E7%84%B6%E8%AA%9E%E8%A8%80%E8%99%95%E7%90%86%E5%85%A5%E9%96%80-word2vec%E5%B0%8F%E5%AF%A6%E4%BD%9C-f8832d9677c8
   * Youngmi huang, 30 July 2018, accessed 24 June 2019
      * https://medium.com/pyladies-taiwan/nltk-%E5%88%9D%E5%AD%B8%E6%8C%87%E5%8D%97-%E4%BA%8C-%E7%94%B1%E5%A4%96%E8%80%8C%E5%85%A7-%E5%BE%9E%E8%AA%9E%E6%96%99%E5%BA%AB%E5%88%B0%E5%AD%97%E8%A9%9E%E6%8B%86%E8%A7%A3-%E4%B8%8A%E6%89%8B%E7%AF%87-e9c632d2b16a
   * Yeh James, 3 Nov 2017, accessed 24 June 2019
      * https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC3-4%E8%AC%9B-%E6%94%AF%E6%8F%B4%E5%90%91%E9%87%8F%E6%A9%9F-support-vector-machine-%E4%BB%8B%E7%B4%B9-9c6c6925856b

* Packages you use
    * nltk
    * keras
    * word2vec
    * sklearn
    
* Related publications
   * Adrian Colyer, 21 APRIL 2016 , accessed 24 June 2019
      * https://blog.acolyer.org/2016/04/21/the-amazing-power-of-word-vectors/

