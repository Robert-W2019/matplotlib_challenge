# matplotlib_challenge

#Observations and Insights

Number of mice (duplicates removed):

248

Drug Regimen Summary Table:
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mean</th>
      <th>Median</th>
      <th>Variance</th>
      <th>Standard Deviation</th>
      <th>SEM</th>
    </tr>
    <tr>
      <th>Drug Regimen</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Capomulin</th>
      <td>40.675741</td>
      <td>41.557809</td>
      <td>24.947764</td>
      <td>4.994774</td>
      <td>0.329346</td>
    </tr>
    <tr>
      <th>Ceftamin</th>
      <td>52.591172</td>
      <td>51.776157</td>
      <td>39.290177</td>
      <td>6.268188</td>
      <td>0.469821</td>
    </tr>
    <tr>
      <th>Infubinol</th>
      <td>52.884795</td>
      <td>51.820584</td>
      <td>43.128684</td>
      <td>6.567243</td>
      <td>0.492236</td>
    </tr>
    <tr>
      <th>Ketapril</th>
      <td>55.235638</td>
      <td>53.698743</td>
      <td>68.553577</td>
      <td>8.279709</td>
      <td>0.603860</td>
    </tr>
    <tr>
      <th>Naftisol</th>
      <td>54.331565</td>
      <td>52.509285</td>
      <td>66.173479</td>
      <td>8.134708</td>
      <td>0.596466</td>
    </tr>
    <tr>
      <th>Placebo</th>
      <td>54.033581</td>
      <td>52.288934</td>
      <td>61.168083</td>
      <td>7.821003</td>
      <td>0.581331</td>
    </tr>
    <tr>
      <th>Propriva</th>
      <td>52.320930</td>
      <td>50.446266</td>
      <td>43.852013</td>
      <td>6.622085</td>
      <td>0.544332</td>
    </tr>
    <tr>
      <th>Ramicane</th>
      <td>40.216745</td>
      <td>40.673236</td>
      <td>23.486704</td>
      <td>4.846308</td>
      <td>0.320955</td>
    </tr>
    <tr>
      <th>Stelasyn</th>
      <td>54.233149</td>
      <td>52.431737</td>
      <td>59.450562</td>
      <td>7.710419</td>
      <td>0.573111</td>
    </tr>
    <tr>
      <th>Zoniferol</th>
      <td>53.236507</td>
      <td>51.818479</td>
      <td>48.533355</td>
      <td>6.966589</td>
      <td>0.516398</td>
    </tr>
  </tbody>
</table>
</div>



#Bar and Pie Charts

Bar Plot - total number of measurements taken on each drug regimen:



Pie Plot - distribution of female versus male mice


#Quartiles, Outliers and Boxplots

Regimen IQR, Lower Bound, Upper Bound, and Number of Outliers (Capomulin, Ramicane, Infubinol, and Ceftamin):


    IQR for Capomulin: 7.781863460000004
    Lower Bound for Capomulin: 20.70456164999999
    Upper Bound for Capomulin: 51.83201549
    Number of Capomulin outliers: 0
    IQR for Ramicane: 9.098536719999998
    Lower Bound for Ramicane: 17.912664470000003
    Upper Bound for Ramicane: 54.30681135
    Number of Ramicane outliers: 0
    IQR for Infubinol: 11.477135160000003
    Lower Bound for Infubinol: 36.83290494999999
    Upper Bound for Infubinol: 82.74144559000001
    Number of Infubinol outliers: 1
    IQR for Ceftamin: 15.577752179999997
    Lower Bound for Ceftamin: 25.355449580000002
    Upper Bound for Ceftamin: 87.66645829999999
    Number of Ceftamin outliers: 0

Box Plot - Final Tumor Volume by Regimens:


#Line and Scatter Plots

Line Plot - tumor volume vs. time point for a mouse treated with Capomulin


Scatter Plot - average tumor volume vs. mouse weight for the Capomulin regimen


#Correlation and Regression

Plot of the correlation coefficient and linear regression model (Average Tumor Volume by Weight):


Correlation between mouse weight and the average tumor volume for the the Capomulin Regimen:

The correlation coefficient between mouse weight and the average tumor volume for the the Capomulin Regimen is 0.84



