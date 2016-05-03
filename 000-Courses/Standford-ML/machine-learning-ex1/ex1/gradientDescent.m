function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
% =============================================================================
% Course: Machine Learning
% Prof. : Andrew Ng
% Student: Bruno Fraga
% Date: 2016-01-10
%
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha
%
%Example of use: 
%   X = [ones(size(load('ex1data1.txt'),1), 1), load('ex1data1.txt')(:,1)];...
%   y = load('ex1data1.txt')(:,2);...
%   theta = zeros(2, 1);...
%   alpha = 0.01;...
%   num_iters = 1500;...
%   [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters);
%
% =============================================================================

% Initialize some useful values
m = length(y); % number of training examples
n = length(theta);
temp = zeros(n,1);
J_history = zeros(num_iters, 1);


for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %
    h = (theta'*X')';
    for parameter_index = 1:n
      temp(parameter_index, 1) = theta(parameter_index,1) - ...
      (alpha/m)*sum((h-y).*X(:,parameter_index));
    end
    theta = temp;





    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);

end

%plot(J_history)
%xlabel('Number of iterations')
%ylabel('J(theta)')

end
