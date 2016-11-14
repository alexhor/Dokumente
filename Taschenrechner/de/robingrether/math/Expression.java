package de.robingrether.math;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public abstract class Expression {
	
	public abstract double evaluate();
	
	private static Pattern linePattern = Pattern.compile("(?:\\(\\s*([0-9.#]*)\\s*(\\+|-)\\s*([0-9.#]+)\\s*\\))|(?:([0-9.#]+)\\s*(\\+|-)\\s*([0-9.#]+))");
	private static Pattern pointPattern = Pattern.compile("(?:\\(\\s*([0-9.#]+)\\s*(\\*|\\/)\\s*([0-9.#]+)\\s*\\))|(?:([0-9.#]+)\\s*(\\*|\\/)\\s*([0-9.#]+))");
	private static Pattern powerPattern = Pattern.compile("(?:\\(\\s*([0-9.#]+)\\s*\\^\\s*([0-9.#]+)\\s*\\))|(?:([0-9.#]+)\\s*\\^\\s*([0-9.#]+))");
	private static Pattern fixedValuePattern = Pattern.compile("\\(?\\s*([\\+-]?\\s*[0-9.#]+)\\s*\\)?");
	
	public static Expression parse(String expression) {
		return parse(expression.trim(), new ArrayList<Expression>());
	}
	
	private static Expression parse(String expression, List<Expression> embedded) {
		boolean ret = false;
		Expression exp1, exp2;
		
		Matcher matcher = powerPattern.matcher(expression);
		while(matcher.find()) {
			ret = true;
			if(matcher.group().startsWith("(")) {
				exp1 = matcher.group(1).startsWith("#") ? embedded.get(Integer.parseInt(matcher.group(1).substring(1))) : new FixedValueExpression(Double.parseDouble(matcher.group(1)));
				exp2 = matcher.group(2).startsWith("#") ? embedded.get(Integer.parseInt(matcher.group(2).substring(1))) : new FixedValueExpression(Double.parseDouble(matcher.group(2)));
			} else {
				exp1 = matcher.group(3).startsWith("#") ? embedded.get(Integer.parseInt(matcher.group(3).substring(1))) : new FixedValueExpression(Double.parseDouble(matcher.group(3)));
				exp2 = matcher.group(4).startsWith("#") ? embedded.get(Integer.parseInt(matcher.group(4).substring(1))) : new FixedValueExpression(Double.parseDouble(matcher.group(4)));
			}
			embedded.add(new PowerExpression(exp1, exp2));
			expression = matcher.replaceFirst("#" + (embedded.size() - 1));
			matcher.reset(expression);
		}
		
		matcher = pointPattern.matcher(expression);
		while(matcher.find()) {
			ret = true;
			if(matcher.group().startsWith("(")) {
				exp1 = matcher.group(1).startsWith("#") ? embedded.get(Integer.parseInt(matcher.group(1).substring(1))) : new FixedValueExpression(Double.parseDouble(matcher.group(1)));
				exp2 = matcher.group(3).startsWith("#") ? embedded.get(Integer.parseInt(matcher.group(3).substring(1))) : new FixedValueExpression(Double.parseDouble(matcher.group(3)));
				embedded.add(matcher.group(2).equals("*") ? new MultiplicationExpression(exp1, exp2) : new DivisionExpression(exp1, exp2));
			} else {
				exp1 = matcher.group(4).startsWith("#") ? embedded.get(Integer.parseInt(matcher.group(4).substring(1))) : new FixedValueExpression(Double.parseDouble(matcher.group(4)));
				exp2 = matcher.group(6).startsWith("#") ? embedded.get(Integer.parseInt(matcher.group(6).substring(1))) : new FixedValueExpression(Double.parseDouble(matcher.group(6)));
				embedded.add(matcher.group(5).equals("*") ? new MultiplicationExpression(exp1, exp2) : new DivisionExpression(exp1, exp2));
			}
			expression = matcher.replaceFirst("#" + (embedded.size() - 1));
			matcher.reset(expression);
		}
		
		matcher = linePattern.matcher(expression);
		while(matcher.find()) {
			ret = true;
			if(matcher.group().startsWith("(")) {
				exp1 = matcher.group(1).isEmpty() ? new FixedValueExpression(0.0) : matcher.group(1).startsWith("#") ? embedded.get(Integer.parseInt(matcher.group(1).substring(1))) : new FixedValueExpression(Double.parseDouble(matcher.group(1)));
				exp2 = matcher.group(3).startsWith("#") ? embedded.get(Integer.parseInt(matcher.group(3).substring(1))) : new FixedValueExpression(Double.parseDouble(matcher.group(3)));
				embedded.add(matcher.group(2).equals("+") ? new AdditionExpression(exp1, exp2) : new SubtractionExpression(exp1, exp2));
			} else {
				exp1 = matcher.group(4).startsWith("#") ? embedded.get(Integer.parseInt(matcher.group(4).substring(1))) : new FixedValueExpression(Double.parseDouble(matcher.group(4)));
				exp2 = matcher.group(6).startsWith("#") ? embedded.get(Integer.parseInt(matcher.group(6).substring(1))) : new FixedValueExpression(Double.parseDouble(matcher.group(6)));
				embedded.add(matcher.group(5).equals("+") ? new AdditionExpression(exp1, exp2) : new SubtractionExpression(exp1, exp2));
			}
			expression = matcher.replaceFirst("#" + (embedded.size() - 1));
			matcher.reset(expression);
		}
		if(ret) return parse(expression, embedded);
		
		matcher = fixedValuePattern.matcher(expression);
		if(matcher.matches()) {
			return matcher.group(1).startsWith("#") ? embedded.get(Integer.parseInt(matcher.group(1).substring(1))) : new FixedValueExpression(Double.parseDouble(matcher.group(1).replace(" ", "")));
		} else {
			throw new IllegalArgumentException("Bad expression");
		}
		
	}
	
	public static void main(String[] args) {
		try {
			System.out.println(parse(" 2 ^ (+1) ").evaluate());
		} catch(IllegalArgumentException e) {
			System.err.println(e.getMessage());
		}
	}
	
}