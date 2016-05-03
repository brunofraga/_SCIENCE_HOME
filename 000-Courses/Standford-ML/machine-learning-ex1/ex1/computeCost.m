function J = computeCost(X, y, theta)
% =============================================================================
% Course: Machine Learning
% Prof. : Andrew Ng
% Student: Bruno Fraga
% Date: 2016-01-10
%
%COMPUTECOST Compute cost for linear regression
%   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y
%
%Example of use: 
%   X = [ones(size(load('ex1data1.txt'),1), 1), load('ex1data1.txt')(:,1)];...
%   y = load('ex1data1.txt')(:,2);...
%   theta = zeros(2, 1);...
%   J = computeCost(X, y, theta)
%
% =============================================================================

% Initialize some useful values
m = length(y); % number of training examples
h = zeros(m,1);

% You need to return the following variables correctly 
J = 0;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta
%               You should set J to the cost.

h = (theta'*X')';
J = (1/(2*m))*sum((h - y).^2);

% =========================================================================

end
