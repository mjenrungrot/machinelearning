function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta


J = 0;
for row = 1:m
    J += -y(row,1) * log(sigmoid(theta' * X(row,:)'));
    J += -(1 - y(row,1)) * log(1 - sigmoid(theta' * X(row,:)' ));
end
J /= m;
J += lambda/(2*m) * sum(theta(2:size(theta),1) .^ 2);

for i = 1:size(theta)(1,1)
    for row = 1:m
        grad(i,1) += (1/m) * (sigmoid(theta' * X(row,:)') - y(row,1)) * X(row,i);
    end
    if i > 1
        grad(i,1) += lambda/m * theta(i,1);
    end
end

% =============================================================

end
