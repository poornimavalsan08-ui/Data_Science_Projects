{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bbf41dfd-a634-4f13-9870-5cf5afbad679",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d1ee7a4f-f4e1-41a5-8ef8-90e0024f99a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        Channel  Impressions  Clicks  Conversions   Cost  Revenue\n",
      "0       Organic        52000    4100          620   3200    27000\n",
      "1      Paid Ads        88000    6700          540  14000    33000\n",
      "2  Social Media        64000    4800          390   8000    20000\n",
      "3         Email        31000    2600          720   2100    24000\n",
      "4       Organic        50000    4000          600   3000    25000\n"
     ]
    }
   ],
   "source": [
    "data=pd.read_csv(r\"C:\\Users\\Lenovo\\Downloads\\marketing_data.csv\")\n",
    "print(data.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5a4c2987-9689-4b2d-a4ee-69d68b0b55c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['CTR'] = data['Clicks'] / data['Impressions']\n",
    "data['ConversionRate']=data['Conversions']/data['Clicks']\n",
    "data['CPA']= data['Cost'] / data['Conversions']\n",
    "data['ROI'] = (data['Revenue'] - data['Cost']) / data['Cost']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9d1936f3-25aa-4c7d-9a62-88b2840d660a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Channel Performance Summary:\n",
      "                Impressions       Clicks  Conversions          Cost  \\\n",
      "Channel                                                              \n",
      "Email         33000.000000  2707.142857   730.000000   2221.428571   \n",
      "Organic       54625.000000  4218.750000   628.125000   3237.500000   \n",
      "Paid Ads      91000.000000  6968.750000   565.000000  15037.500000   \n",
      "Social Media  63857.142857  4800.000000   392.857143   8000.000000   \n",
      "\n",
      "                   Revenue       CTR  ConversionRate        CPA        ROI  \n",
      "Channel                                                                     \n",
      "Email         24500.000000  0.082001        0.270260   3.038867  10.033145  \n",
      "Organic       27125.000000  0.077324        0.148907   5.152232   7.381341  \n",
      "Paid Ads      35125.000000  0.076582        0.081065  26.601805   1.337146  \n",
      "Social Media  20185.714286  0.075175        0.081783  20.367575   1.527315  \n"
     ]
    }
   ],
   "source": [
    "# Channel Summary\n",
    "channel_summary = data.groupby('Channel').mean(numeric_only=True)\n",
    "print(\"\\nChannel Performance Summary:\\n\", channel_summary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d619d44d-2107-47b6-a37d-98e8fd192522",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Best ROI Row:\n",
      "Channel               Email\n",
      "Impressions           31000\n",
      "Clicks                 2600\n",
      "Conversions             720\n",
      "Cost                   2100\n",
      "Revenue               24000\n",
      "CTR                0.083871\n",
      "ConversionRate     0.276923\n",
      "CPA                2.916667\n",
      "ROI               10.428571\n",
      "Name: 3, dtype: object\n"
     ]
    }
   ],
   "source": [
    "# Best ROI Row\n",
    "print(\"\\nBest ROI Row:\")\n",
    "print(data.loc[data['ROI'].idxmax()])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2fe2fa49-f01b-4916-b42e-cde67c368c27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Best Conversion Rate Row:\n",
      "Channel              Email\n",
      "Impressions          30000\n",
      "Clicks                2400\n",
      "Conversions            690\n",
      "Cost                  2000\n",
      "Revenue              22000\n",
      "CTR                   0.08\n",
      "ConversionRate      0.2875\n",
      "CPA               2.898551\n",
      "ROI                   10.0\n",
      "Name: 7, dtype: object\n"
     ]
    }
   ],
   "source": [
    "# Best Conversion Rate Row\n",
    "print(\"\\nBest Conversion Rate Row:\")\n",
    "print(data.loc[data['ConversionRate'].idxmax()])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e1d7603f-3af0-435e-9c6e-847d9605eb19",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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5/KCBQtq4cKF6tGjR67vc/lE0yZNmtzUHP95gutlx48fl+T6l3ClSpUUExOjjz76SDExMVq8eLGGDRt2zW/YNGvWTK+//roWLlyo5s2b39SMuVm9erWOHj2q+Ph4594OSTpz5ozbtnEloaGhkqTBgwerbdu2ua5TtWpVj88B5EXs+QC8yOjRoxUcHKw333xT2dnZkv7aA9G1a1ctX75cc+fOzfEzP//8s959913VqFHjhk/ovOzs2bNavHixy7I5c+aoQIECeuSRR1yW9+vXTzt37lSnTp3k4+Oj7t27X/P977nnHsXExGjatGlavXp1ruskJCToyJEjNzT35cNMl/dKXDZlypQbep+bUbVqVVWuXFmJiYmqW7durg9/f3+PzwHkRez5ALxIcHCwBg8erNdee01z5sxxfrNj7Nix2rdvnzp27Kh169apVatW8vX11aZNmzRmzBj5+/vrq6++uulrfISEhKhnz546cuSIqlSpom+++UYff/yxevbsmePrr02aNFH16tW1Zs0adezYUWFhYde1jdmzZ6t58+aKiYlR165dFRMTo+DgYB07dkxLlixRXFyctm3blmN7V9OgQQMFBwerR48eGjp0qAoVKqTPPvvM2MXKpkyZopiYGDVr1kydO3fWnXfeqVOnTmnPnj3avn27vvjiCyNzAHkNez4AL9OnTx+VLVtWb731lvM6G8WLF9eKFSv04Ycfatu2bXrqqacUExOjWbNm6YUXXtCOHTtuaRd/qVKlNGfOHM2aNUutW7fWvHnz9Prrr2v8+PG5rv/0009L0g2daBoaGqoNGzZozJgxSkxM1PPPP69GjRrp5ZdfVnp6uhYvXqy77777huYOCQnR119/rWLFiqljx47q2rWr/Pz8ct1D5AnR0dHasmWLgoKC1L9/fzVu3Fg9e/bUypUr1bhxYyMzAHmRw7Isy+4hAOQtdevWlcPh0NatW+0eBUAexGEXANclNTVVP/74o/79739r27ZtWrBggd0jAcijiA8A12X79u2Kjo5WSEiIhg4detMntwIAh10AAIBRnHAKAACMIj4AAIBRxAcAADDK6044zc7O1tGjR+Xv73/TN8kCAABmWZals2fPqnTp0ipQ4Or7NrwuPo4ePXrTN8cCAAD2Sk5OVpkyZa66jtfFx+V7ISQnJysgIMDmaQAAwPVITU1VRETEdd3TyOvi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Dz/80GU7lw+HjBkzRuHh4QoJCVFsbKwuXbrkXKd8+fIaMWKEunbtKn9/f5UtW1ZTp051eZ/ffvtN7du3V3BwsEJCQtSmTRsdOnTIM384ANyK+ACgU6dOadmyZYqNjVXx4sVzvB4UFOT89bBhw/T0009r586datGihTp06KBTp05JkrKzs1WmTBnNmzdPu3fv1ptvvqnXX39d8+bNc3m/NWvW6ODBg1qzZo1mzZqlmTNnaubMmS7rvP/++6pbt65++OEH9erVSz179nTufUlPT1d0dLT8/Py0bt06bdiwQX5+fmrevLkuXrzo3j8cAO5nAbjtbd682ZJkzZ8//6rrSbL+8Y9/OJ+npaVZDofDWrp06RV/plevXtaTTz7pfN6pUyerXLlyVmZmpnPZU089ZbVv3975vFy5clbHjh2dz7Ozs62wsDBr0qRJlmVZ1rRp06yqVata2dnZznUyMjKsokWLWsuXL3dup02bNtf4nQOwA+d8AJD1/++y4HA4rrlurVq1nL8uXry4/P39deLECeeyyZMn65NPPtHhw4d1/vx5Xbx4UbVr13Z5jxo1arjcByM8PFy7du264nYcDodKlSrl3M62bdt04MAB+fv7u/zMhQsXdPDgwWv+HgDYi/gAoMqVK8vhcGjPnj3X/HpqoUKFXJ47HA5lZ2dLkubNm6eXX35Z77//vurXry9/f3+999572rx583W/x/Wsk52drXvvvVefffZZjvnuuOOOq84PwH7EBwCVKFFCzZo100cffaS+ffvmOO/jzJkzLud9XMn69evVoEED9erVy7nME3si7rnnHs2dO1dhYWEKCAhw+/sD8CxOOAUgSZo4caKysrJUr149ffXVV9q/f7/27Nmj8ePHq379+tf1HpUqVVJCQoKWL1+un3/+WUOGDNHWrVvdPmuHDh0UGhqqNm3aaP369UpKStLatWvVr18//frrr27fHgD3Ij4ASJIiIyO1fft2RUdH65VXXlFUVJSaNGmiVatWadKkSdf1Hj169FDbtm3Vvn173X///Tp58qTLXhB3KVasmNatW6eyZcuqbdu2qlatmrp27arz58+zJwTIAxzW5TPNAAAADGDPBwAAMIr4AAAARhEfAADAKOIDAAAYRXwAAACjiA8AAGAU8QEAAIwiPgAAgFHEBwAAMIr4AAAARhEfAADAqP8HB8ojpkDMdfUAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# ROI Graph\n",
    "data.groupby('Channel')['ROI'].mean().plot(kind='bar')\n",
    "plt.title(\"ROI by Channel\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a19c64eb-bea4-4158-8903-ab757b53f333",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Conversion Rate Graph\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
