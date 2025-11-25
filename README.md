# A1 Motorcycle License Test Data

ベトナムのA1バイク免許試験問題データとHTML解析ツールのリポジトリです。

## 📋 概要

このリポジトリには、ベトナムのA1バイク免許試験に関する以下のデータとツールが含まれています：

- **250問の試験問題データ**（JSON形式）
- **元のHTMLファイル**



## 問題データ統計

**総問題数**: 250問

### 正解番号分布

| 選択肢数 | 1番 | 2番 | 3番 | 4番 | 合計 |
|---------|-----|-----|-----|-----|------|
| 2択 | 21 | 14 | - | - | 35 |
| 3択 | 46 | 50 | 41 | - | 137 |
| 4択 | 18 | 13 | 25 | 22 | 78 |

### 画像問題 (69問)

| 選択肢数 | 1番 | 2番 | 3番 | 4番 | 合計 |
|---------|-----|-----|-----|-----|------|
| 2択 | 3 | 4 | - | - | 7 |
| 3択 | 12 | 15 | 8 | - | 35 |
| 4択 | 9 | 7 | 9 | 2 | 27 |

### キーワード分布（上位10位）



### Required問題分布

| Required | 2択 | 3択 | 4択 | 合計 |
|----------|-----|-----|-----|------|
| 必須 | 1 | 9 | 10 | 20 |
| 通常 | 34 | 128 | 68 | 230 |

#### 必須問題の正解番号分布

| 選択肢数 | 1番 | 2番 | 3番 | 4番 | 合計 |
|---------|-----|-----|-----|-----|------|
| 2択 | 0 | 1 | - | - | 1 |
| 3択 | 3 | 4 | 2 | - | 9 |
| 4択 | 1 | 4 | 2 | 3 | 10 |
| 合計 | 4 | 9 | 4 | 3 | 20 |

#### 通常問題の正解番号分布

| 選択肢数 | 1番 | 2番 | 3番 | 4番 | 合計 |
|---------|-----|-----|-----|-----|------|
| 2択 | 21 | 13 | - | - | 34 |
| 3択 | 43 | 46 | 39 | - | 128 |
| 4択 | 17 | 9 | 23 | 19 | 68 |
| 合計 | 81 | 68 | 62 | 19 | 230 |


---

#### 画像問題を除いた3択問題の3択目短文の正解割合

| カテゴリ | 問題数 |  | 正解率 |
|---------|--------|------------------|--------|
| 3択目が短文 | 41問 | 14問（3番が正解） | 34.1% |
| 3択目が長文 | 54問 | 20問（2番が正解） | 37.0% |
| 合計 | 95問 | - | - |

**注**: 3択目が長文の問題では2番を選択する戦略のため、2番が正解の問題数を表示


## テスト手順

### 戦略ルールの問題数

| ルール | 必須 | 画像 | 2択 | 3択 | 4択 | 末回答短 | 問題文100↑ | 1 | 2 | 3 | 4 | 合計 |
|--------|------|------|-----|-----|-----|----------|------------|---|---|---|---|------|
| ルール1:必須 | ● |  |  |  |  |  |  |  |  |  |  | 20 |
| ルール2:2択 |  |  | ● |  |  |  |  | 21 | 13 |  |  | 34 |
| ルール3a:3択画像 |  | ● |  | ● |  |  |  | 12 | 12 | 9 |  | 33 |
| ルール3b:4択画像 |  | ● |  |  | ● |  |  | 7 | 6 | 7 | 2 | 22 |
| ルール4: 3択で選択肢3が「Cả hai ý trên.」 |  |  |  | ● |  |  |  | 6 | 5 | 14 | 0 | 25 |
| ルール5: 3択で選択肢3が100文字以上 |  |  |  | ● |  |  |  | 7 | 1 | 1 | 0 | 9 |
| ルール6: 3択で選択肢3が短く問題文100文字以上 |  |  |  | ● |  | ● | ● | 5 | 2 | 2 | 0 | 9 |
| ルール7: 3択でshort_last_option=falseかつ問題文50文字以下 |  |  |  | ● |  |  | ● | 3 | 1 | 3 | 0 | 7 |
| ルール8: 残りの3択 |  |  |  | ● |  |  |  | 11 | 23 | 11 |  | 45 |
| ルール9: 4択で選択肢４が短い |  |  |  |  | ● | ● |  | 5 | 3 | 2 | 15 | 25 |
| ルール10: 残りの4択 |  |  |  |  | ● |  |  | 4 | 2 | 13 | 2 | 21 |
| **合計** | | | | | | | | **85** | **77** | **66** | **22** | **250** |

### 戦略ルールの説明

#### 各ルールの回答方法

| ルール       | 回答方法        | 正解率      | 説明                                                |
| --------- | ----------- | -------- | ------------------------------------------------- |
| **ルール1**  | **暗記**      | **100%** | **必須問題（Required=true）は暗記必須で正解**                   |
| **ルール2**  | **暗記**      | **100%** | **2択問題は暗記必須で正解**                                  |
| **ルール3a** | **暗記**      | **80%**  | **3択の画像問題は暗記必須で正解**                               |
| **ルール3b** | **暗記**      | **80%**  | **4択の画像問題は暗記必須で正解**                               |
| **ルール4**  | **選択肢3を選択** | **56%**  | **3択で選択肢3が「Cả hai ý trên.」の場合は選択肢3**              |
| **ルール5**  | **選択肢1を選択** | **78%**  | **3択で選択肢3が100文字以上の場合は選択肢1**                       |
| **ルール6**  | **選択肢1を選択** | **55%**  | **3択でshort_last_option=trueかつ問題文100文字以上の場合は選択肢1** |
| **ルール7**  | **選択肢1を選択** | **42%**  | **3択でshort_last_option=falseかつ問題文50文字以下の場合は選択肢1** |
| **ルール8**  | **選択肢2を選択** | **51%**  | **残りの3択問題は選択肢2を選択**                               |
| **ルール9**  | **選択肢4を選択** | **60%**  | **4択で選択肢4が短い場合は選択肢4**                             |
| **ルール10** | **選択肢3を選択** | **62%**  | **残りの4択問題は選択肢3を選択**                               |



### 戦略の流れ
1. 必須問題（Required=true）の20問は暗記で正解する
250-20=230

2. 2択問題は、少ない２の解答の問題のみ暗記して正解する
2択の問題は合計35問。内、必須問題1問,回答1が21問,回答2が13問。
230-34=196

3. 画像問題は絵で覚えるから暗記できる。
画像問題は合計69問。内、必須かつ画像問題が１問、必須問題が7問、2択問題が6問。
196-(69-1-7-6)=141

4. 3択で選択肢3が「Cả hai ý trên.」の場合は選択肢3を選ぶ

---

## 全250問の問題マップ

以下のテーブルは全250問を一覧表示しています：
- **1行目**: 問題ID（1〜250）
- **2行目**: カテゴリ（必須問題、画像付き2/3/4択、画像なし2/3/4択）
- **3行目**: ルール（今後追加予定）
- **4行目**: 正解番号

<table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; font-size: 12px;">
  <tr>
    <th>項目</th>
    <td align="center">1</td>
    <td align="center">2</td>
    <td align="center">3</td>
    <td align="center">4</td>
    <td align="center">5</td>
    <td align="center">6</td>
    <td align="center">7</td>
    <td align="center">8</td>
    <td align="center">9</td>
    <td align="center">10</td>
    <td align="center">11</td>
    <td align="center">12</td>
    <td align="center">13</td>
    <td align="center">14</td>
    <td align="center">15</td>
    <td align="center">16</td>
    <td align="center">17</td>
    <td align="center">18</td>
    <td align="center">19</td>
    <td align="center">20</td>
    <td align="center">21</td>
    <td align="center">22</td>
    <td align="center">23</td>
    <td align="center">24</td>
    <td align="center">25</td>
    <td align="center">26</td>
    <td align="center">27</td>
    <td align="center">28</td>
    <td align="center">29</td>
    <td align="center">30</td>
    <td align="center">31</td>
    <td align="center">32</td>
    <td align="center">33</td>
    <td align="center">34</td>
    <td align="center">35</td>
    <td align="center">36</td>
    <td align="center">37</td>
    <td align="center">38</td>
    <td align="center">39</td>
    <td align="center">40</td>
    <td align="center">41</td>
    <td align="center">42</td>
    <td align="center">43</td>
    <td align="center">44</td>
    <td align="center">45</td>
    <td align="center">46</td>
    <td align="center">47</td>
    <td align="center">48</td>
    <td align="center">49</td>
    <td align="center">50</td>
    <td align="center">51</td>
    <td align="center">52</td>
    <td align="center">53</td>
    <td align="center">54</td>
    <td align="center">55</td>
    <td align="center">56</td>
    <td align="center">57</td>
    <td align="center">58</td>
    <td align="center">59</td>
    <td align="center">60</td>
    <td align="center">61</td>
    <td align="center">62</td>
    <td align="center">63</td>
    <td align="center">64</td>
    <td align="center">65</td>
    <td align="center">66</td>
    <td align="center">67</td>
    <td align="center">68</td>
    <td align="center">69</td>
    <td align="center">70</td>
    <td align="center">71</td>
    <td align="center">72</td>
    <td align="center">73</td>
    <td align="center">74</td>
    <td align="center">75</td>
    <td align="center">76</td>
    <td align="center">77</td>
    <td align="center">78</td>
    <td align="center">79</td>
    <td align="center">80</td>
    <td align="center">81</td>
    <td align="center">82</td>
    <td align="center">83</td>
    <td align="center">84</td>
    <td align="center">85</td>
    <td align="center">86</td>
    <td align="center">87</td>
    <td align="center">88</td>
    <td align="center">89</td>
    <td align="center">90</td>
    <td align="center">91</td>
    <td align="center">92</td>
    <td align="center">93</td>
    <td align="center">94</td>
    <td align="center">95</td>
    <td align="center">96</td>
    <td align="center">97</td>
    <td align="center">98</td>
    <td align="center">99</td>
    <td align="center">100</td>
    <td align="center">101</td>
    <td align="center">102</td>
    <td align="center">103</td>
    <td align="center">104</td>
    <td align="center">105</td>
    <td align="center">106</td>
    <td align="center">107</td>
    <td align="center">108</td>
    <td align="center">109</td>
    <td align="center">110</td>
    <td align="center">111</td>
    <td align="center">112</td>
    <td align="center">113</td>
    <td align="center">114</td>
    <td align="center">115</td>
    <td align="center">116</td>
    <td align="center">117</td>
    <td align="center">118</td>
    <td align="center">119</td>
    <td align="center">120</td>
    <td align="center">121</td>
    <td align="center">122</td>
    <td align="center">123</td>
    <td align="center">124</td>
    <td align="center">125</td>
    <td align="center">126</td>
    <td align="center">127</td>
    <td align="center">128</td>
    <td align="center">129</td>
    <td align="center">130</td>
    <td align="center">131</td>
    <td align="center">132</td>
    <td align="center">133</td>
    <td align="center">134</td>
    <td align="center">135</td>
    <td align="center">136</td>
    <td align="center">137</td>
    <td align="center">138</td>
    <td align="center">139</td>
    <td align="center">140</td>
    <td align="center">141</td>
    <td align="center">142</td>
    <td align="center">143</td>
    <td align="center">144</td>
    <td align="center">145</td>
    <td align="center">146</td>
    <td align="center">147</td>
    <td align="center">148</td>
    <td align="center">149</td>
    <td align="center">150</td>
    <td align="center">151</td>
    <td align="center">152</td>
    <td align="center">153</td>
    <td align="center">154</td>
    <td align="center">155</td>
    <td align="center">156</td>
    <td align="center">157</td>
    <td align="center">158</td>
    <td align="center">159</td>
    <td align="center">160</td>
    <td align="center">161</td>
    <td align="center">162</td>
    <td align="center">163</td>
    <td align="center">164</td>
    <td align="center">165</td>
    <td align="center">166</td>
    <td align="center">167</td>
    <td align="center">168</td>
    <td align="center">169</td>
    <td align="center">170</td>
    <td align="center">171</td>
    <td align="center">172</td>
    <td align="center">173</td>
    <td align="center">174</td>
    <td align="center">175</td>
    <td align="center">176</td>
    <td align="center">177</td>
    <td align="center">178</td>
    <td align="center">179</td>
    <td align="center">180</td>
    <td align="center">181</td>
    <td align="center">182</td>
    <td align="center">183</td>
    <td align="center">184</td>
    <td align="center">185</td>
    <td align="center">186</td>
    <td align="center">187</td>
    <td align="center">188</td>
    <td align="center">189</td>
    <td align="center">190</td>
    <td align="center">191</td>
    <td align="center">192</td>
    <td align="center">193</td>
    <td align="center">194</td>
    <td align="center">195</td>
    <td align="center">196</td>
    <td align="center">197</td>
    <td align="center">198</td>
    <td align="center">199</td>
    <td align="center">200</td>
    <td align="center">201</td>
    <td align="center">202</td>
    <td align="center">203</td>
    <td align="center">204</td>
    <td align="center">205</td>
    <td align="center">206</td>
    <td align="center">207</td>
    <td align="center">208</td>
    <td align="center">209</td>
    <td align="center">210</td>
    <td align="center">211</td>
    <td align="center">212</td>
    <td align="center">213</td>
    <td align="center">214</td>
    <td align="center">215</td>
    <td align="center">216</td>
    <td align="center">217</td>
    <td align="center">218</td>
    <td align="center">219</td>
    <td align="center">220</td>
    <td align="center">221</td>
    <td align="center">222</td>
    <td align="center">223</td>
    <td align="center">224</td>
    <td align="center">225</td>
    <td align="center">226</td>
    <td align="center">227</td>
    <td align="center">228</td>
    <td align="center">229</td>
    <td align="center">230</td>
    <td align="center">231</td>
    <td align="center">232</td>
    <td align="center">233</td>
    <td align="center">234</td>
    <td align="center">235</td>
    <td align="center">236</td>
    <td align="center">237</td>
    <td align="center">238</td>
    <td align="center">239</td>
    <td align="center">240</td>
    <td align="center">241</td>
    <td align="center">242</td>
    <td align="center">243</td>
    <td align="center">244</td>
    <td align="center">245</td>
    <td align="center">246</td>
    <td align="center">247</td>
    <td align="center">248</td>
    <td align="center">249</td>
    <td align="center">250</td>
  </tr>
  <tr>
    <th>カテゴリ</th>
    <td align="center" colspan="20"><strong>必須問題</strong></td>
    <td align="center" colspan="3"><strong>画像なし3択</strong></td>
    <td align="center" colspan="3"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="2"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="2"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="2"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="3"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="2"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="2"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="2"><strong>画像なし2択</strong></td>
    <td align="center" colspan="8"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="2"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="2"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="2"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="2"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="2"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="3"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="3"><strong>画像付き4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="2"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="2"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="4"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="3"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="2"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="2"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="4"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="3"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="1"><strong>画像付き2択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き2択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像付き2択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="2"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像付き2択</strong></td>
    <td align="center" colspan="4"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="3"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="3"><strong>画像なし4択</strong></td>
    <td align="center" colspan="2"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="2"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き2択</strong></td>
    <td align="center" colspan="2"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="2"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="2"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="2"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き2択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
    <td align="center" colspan="1"><strong>画像付き3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし2択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="2"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像なし4択</strong></td>
    <td align="center" colspan="1"><strong>画像なし3択</strong></td>
    <td align="center" colspan="1"><strong>画像付き4択</strong></td>
  </tr>
  <tr>
    <th>ルール</th>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
    <td align="center"></td>
  </tr>
  <tr>
    <th>正解</th>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>1</strong></td>
    <td align="center"><strong>3</strong></td>
    <td align="center"><strong>4</strong></td>
    <td align="center"><strong>2</strong></td>
    <td align="center"><strong>3</strong></td>
  </tr>
</table>
