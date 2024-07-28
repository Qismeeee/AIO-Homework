import numpy as np

def get_index_from_value(feature_name, list_features):
    return np.where(np.array(list_features) == feature_name.strip())[0][0]

# Create data
def create_train_data():
    data = [
        ['Sunny', 'Hot', 'High', 'Weak', 'no'],
        ['Sunny', 'Hot', 'High', 'Strong', 'no'],
        ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
        ['Overcast', 'Mild', 'High', 'Weak', 'no'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'yes']
    ]
    return np.array(data)

# Compute conditional probability
def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = {}
    list_x_name = []
    
    for i in range(0, train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
        
        x_conditional_probability = {}
        for x_value in x_unique:
            conditional_probs = {}
            for y_value in y_unique:
                count_x_and_y = np.sum((train_data[:, i] == x_value) & (train_data[:, -1] == y_value))
                count_y = np.sum(train_data[:, -1] == y_value)
                if count_y > 0:
                    prob_x_given_y = count_x_and_y / count_y
                else:
                    prob_x_given_y = 0
                conditional_probs[y_value] = prob_x_given_y
            x_conditional_probability[x_value] = conditional_probs
        
        conditional_probability[i] = x_conditional_probability
    
    return conditional_probability, list_x_name

# Train Naive Bayes Model
def train_naive_bayes(train_data):
    prior_probability = compute_prior_probability(train_data)
    conditional_probability, list_x_name = compute_conditional_probability(train_data)
    
    return prior_probability, conditional_probability, list_x_name

# Compute prior probability
def compute_prior_probability(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))
    
    total_instances = train_data.shape[0]
    count_no = np.sum(train_data[:, -1] == 'no')
    count_yes = np.sum(train_data[:, -1] == 'yes')
    
    prior_probability[0] = count_no / total_instances
    prior_probability[1] = count_yes / total_instances
    
    return prior_probability

# Prediction
def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(X[0], list_x_name[0])
    x2 = get_index_from_value(X[1], list_x_name[1])
    x3 = get_index_from_value(X[2], list_x_name[2])
    x4 = get_index_from_value(X[3], list_x_name[3])
    
    p_no = prior_probability[0]
    p_yes = prior_probability[1]
    
    p_no *= conditional_probability[0][list_x_name[0][x1]]['no']
    p_no *= conditional_probability[1][list_x_name[1][x2]]['no']
    p_no *= conditional_probability[2][list_x_name[2][x3]]['no']
    p_no *= conditional_probability[3][list_x_name[3][x4]]['no']
    
    p_yes *= conditional_probability[0][list_x_name[0][x1]]['yes']
    p_yes *= conditional_probability[1][list_x_name[1][x2]]['yes']
    p_yes *= conditional_probability[2][list_x_name[2][x3]]['yes']
    p_yes *= conditional_probability[3][list_x_name[3][x4]]['yes']
    
    if p_no > p_yes:
        y_pred = 'no'
    else:
        y_pred = 'yes'
    
    return y_pred

# Test
train_data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(train_data)

X_test = ['Sunny', 'Cool', 'High', 'Strong']
# Compute P("Outlook" = "Sunny" | Play Tennis = "No")
x1 = get_index_from_value("Sunny", list_x_name[0])
prob_sunny_given_no = conditional_probability[0]['Sunny']['no']
print("P('Outlook' = 'Sunny' | Play Tennis = 'No') =", np.round(prob_sunny_given_no, 2))

# Compute P("Outlook" = "Sunny" | Play Tennis = "Yes")
prob_sunny_given_yes = conditional_probability[0]['Sunny']['yes']
print("P('Outlook' = 'Sunny' | Play Tennis = 'Yes') =", np.round(prob_sunny_given_yes, 2))

X = ['Sunny', 'Cool', 'High', 'Strong']
data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(data)
pred = prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability)

if pred:
    print("Ad should go!")
else:
    print("Ad should not go!")