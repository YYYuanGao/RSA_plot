close all; clear all; clc;
DataDir = '/Users/zhangzirui/Desktop/Code for YUAN';
data = load('C:\Users\Zirui Zhang\Desktop\For Yuan\box and violin plots for Yuan\heatmap/RSA/RSA_PlotData.mat');

datas = data.RSA_Matrix(:,:,1);
datad = data.RSA_Matrix(:,:,2);
datai = data.RSA_Matrix(:,:,3);